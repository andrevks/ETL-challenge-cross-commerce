import random
import sys
import os
import datetime
import json
# sys.path.append('../src')
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
    print(f'\n>>> {output} \n {compOutput}\n')

    assert output == compOutput

def test_get_recent_file():
    shuffledArr = generateRandomNumbers()
    orderedArr = mergeSort(shuffledArr)

    dt_data = datetime.datetime.now()
    day = str(dt_data.strftime("%d-%b-%Y"))
    abs_path = 'C:\\Users\\andre\\PycharmProjects\\flaskProjectETLCrossCommerce\\src\\dataWarehouse\\transformed'
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

def test_transform():
    shuffledArr = generateRandomNumbers(100)

    dt_data = datetime.datetime.now()
    day = str(dt_data.strftime("%d-%b-%Y"))
    abs_path = 'C:\\Users\\andre\\PycharmProjects\\flaskProjectETLCrossCommerce\\src\\dataWarehouse\\extracted'
    savedExtractedFileName = f'{abs_path}\\test_extractedNumbers-{day}.json'

    try:
        json_transformedNumbers = json.dumps(shuffledArr, indent=4)
        with open(savedExtractedFileName , 'w') as outfile:
            outfile.write(json_transformedNumbers)

    except Exception as err:
        print(f'Error in writing file in transform_test: {err}')
    else:
        transform()
        # abs_path = 'C:\\Users\\andre\\PycharmProjects\\flaskProjectETLCrossCommerce\\src\\dataWarehouse\\transformed'
        # savedFileName = f'{abs_path}\\test_transformedNumbers-{day}.json'
        #
        # output = get_recent_file(savedFileName)
        # compOutput = mergeSort(get_recent_file(savedExtractedFileName))
        #
        # assert output == compOutput