from flask import Flask
from flask_restx import Resource, reqparse
from src.server.instance import server
import json

import glob
import os

app, api = server.app, server.api
parser = reqparse.RequestParser()
parser.add_argument('page', required=False)

def read_transform_file():
    # day = '21-Dec-2021'
    # filename = f'src/dataWarehouse/transformed/transformedNumbers-{day}.json'
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
    print(f'latest_file in LOAD: {latest_file}')
    return latest_file


@api.route('/api/', '/')
class Home(Resource):
    def get(self):
        return 'Welcome to the ETL API of NUMBERS'

# @api.route('/api/numbers/<int:page>/')
@api.route('/api/numbers/')
class Load(Resource):
    ''' Load the numbers Extracted and Transformed in previously '''

    def get(self, page=None):
        transformedNumbers = read_transform_file()
        args = parser.parse_args()
        page = args['page']

        if page:
            # '''Return numbers (100) by Page'''
            page = int(page)
            # print(f'Args:{args}')
            numberPerPage = 100
            beginPage = (page - 1) * numberPerPage
            endPage = page * numberPerPage
            return { "numbers": transformedNumbers[beginPage:endPage] }, 200

        # '''Return the first 100 numbers'''
        return transformedNumbers[0:100], 200


