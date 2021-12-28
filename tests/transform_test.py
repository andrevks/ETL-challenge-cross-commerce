import random
import sys
import os
import datetime
import json
from src.transform import mergeSort, get_recent_file, transform

def generateRandomNumbers(max=10):
    shuffledArr = [random.uniform(0.0 , 0.999999999) for x in range(max)]
    return shuffledArr

def test_merge_sort():
    """ Verify the sorting algorithm """
    shuffledArr = generateRandomNumbers()
    output = mergeSort(shuffledArr)

    orderedArr = sorted(shuffledArr , key=float)
    compOutput = orderedArr

    assert output == compOutput

def test_get_recent_file():
    """Verify the function that retrieves the recent extracted file created"""
    shuffledArr = generateRandomNumbers()
    orderedArr = mergeSort(shuffledArr)

    dt_data = datetime.datetime.now()
    day = str(dt_data.strftime("%d-%b-%Y"))
    abs_path = '..\\src\\dataWarehouse\\transformed'
    savedFileName = f'{abs_path}\\test_transformedNumbers-{day}.json'

    try:
        json_transformedNumbers = json.dumps(orderedArr , indent=4)
        with open(savedFileName , 'w') as outfile:
            outfile.write(json_transformedNumbers)

    except Exception as err:
        print(f'Error in writing file in transform_test: {err}')
    else:
        abs_path = f'{abs_path}\\*.json'
        output = get_recent_file(abs_path)
        compOutput = savedFileName
        os.remove(savedFileName)
        assert  output == compOutput