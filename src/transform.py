import json
import time
import os
import glob

def merge(leftArr, rightArr):
    mergedArr = []
    while len(leftArr) > 0 and len(rightArr) > 0:
        if leftArr[0]  < rightArr[0]:
            mergedArr.append(leftArr[0])
            del leftArr[0]
        else:
            mergedArr.append(rightArr[0])
            del rightArr[0]

    while len(leftArr) > 0:
        mergedArr.append(leftArr[0])
        del leftArr[0]

    while len(rightArr) > 0:
        mergedArr.append(rightArr[0])
        del rightArr[0]

    return mergedArr


def mergeSort(arr):
    arrLength = len(arr)
    if arrLength == 1:
        return arr

    mid = int((arrLength - 1) / 2)
    leftArr = arr[0:mid+1]
    rightArr = arr[mid+1:]

    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)

    return merge(leftArr, rightArr)


def get_recent_file(path='src\\dataWarehouse\\extracted\\*.json' ):
    try:
        list_of_files = glob.glob(path)
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
    except ValueError as valueErr:
        print(f'No path file found in this path: {valueErr}')
    except Exception as err:
        print(f'Error ocurred when getting recent file: {err}')


def transform():
    orderedNumbers = []
    try:
        abs_path = 'src\\dataWarehouse'
        save_path = f'{abs_path}\\extracted\\*.json'
        filename = get_recent_file(save_path)
        with open(filename, 'r') as inputFile:
            numbersExtracted = json.load(inputFile)

        print(f'----Before Transforming-----')
        count = 0
        # O(n)
        for number in numbersExtracted:
            count += 1

        print(f'Numbers Extracted: {count}')

        print('>> initiating Transformation...')

        startTime = time.time()
        orderedNumbers = mergeSort(numbersExtracted)
        executionTime = str((time.time() - startTime))

        print("\n-----------------------------------")
        print('Success')
        print(f" Took {executionTime} s to TRANSFORM")
        print("-----------------------------------")
        day = filename.split('extractedNumbers' , 1)[1]
        if 'test' in filename:
            savedFileName = f'{abs_path}\\transformed\\test_transformedNumbers{day}'
        else:
            savedFileName = f'{abs_path}\\transformed\\transformedNumbers{day}'

        json_transformedNumbers = json.dumps(orderedNumbers, indent=4)
        with open(savedFileName, 'w') as outfile:
            outfile.write(json_transformedNumbers)

        print("\n-----------------------------------")
        print(f'>> Transformed NUMBERS were saved in: \n --> {savedFileName}')
        print("-----------------------------------\n")


    except Exception as ex:
        print(f'Error in Transforming: {ex}')


