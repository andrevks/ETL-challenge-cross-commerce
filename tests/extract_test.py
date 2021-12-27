import requests
import json
from requests.exceptions import HTTPError, Timeout
from src.extract import getExtractedNumbersFromPage

def test_getExtractedNumbersFromPage():
    numbersMock = {}
    try:
        filename = 'mock_extracted_numbers.json'
        with open(filename, 'r') as inputFile:
            numbersMock = json.load(inputFile)
            print(numbersMock)
    except Exception as err:
        print(f'Error in opening file: {err}')

    numbers = getExtractedNumbersFromPage(pageNumber=1)
    output = numbers
    compOutput = numbersMock
    assert output == compOutput


