from flask import Flask
from flask_restx import Resource, reqparse
from src.server.instance import server
import json

import glob
import os

app, api = server.app, server.api
parser = reqparse.RequestParser()
parser.add_argument('page', type=int, required=False, default=None)
parser.add_argument('page_size', type=int, required=False, default=100)

def read_transform_file():
    filename = get_recent_file()
    transformedNumbers = []
    try:
        with open(filename, 'r') as inputFile:
            transformedNumbers = json.load(inputFile)
        return transformedNumbers
    except Exception as ex:
        print(f'Error in Open file: {ex}')


def get_recent_file():
    list_of_files = glob.glob('.\\src\\dataWarehouse\\transformed\\*.json')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


@api.route('/api/', '/')
class Home(Resource):
    def get(self):
        return 'Welcome to the ETL API of NUMBERS'

@api.route('/api/numbers/')
class Load(Resource):
    ''' Load the numbers Extracted and Transformed in previously '''

    def get(self):
        transformedNumbers = read_transform_file()
        args = parser.parse_args()
        page = args['page']
        page_size = args['page_size']

        if page_size > 5000:
            return {"error":'The page size should be less than 5000.'}, 400
        elif page_size < 100:
            return {"error":'The page size should be at least 100.'}, 400

        if page:
            # '''Return numbers (100) by Page'''
            page = int(page)
            page_size = int(page_size)
            if page < 1:
                return {"error":'The page should be greater than 0'}, 400
            beginPage = (page - 1) * page_size
            endPage = page * page_size
            return { "numbers": transformedNumbers[beginPage:endPage] }, 200

        # '''Return the first 100 numbers'''
        if transformedNumbers:
            return transformedNumbers[0:page_size], 200



