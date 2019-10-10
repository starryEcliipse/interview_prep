# This is my implementation of the binary search algorithm
# Reference used: https://en.wikipedia.org/wiki/Binary_search_algorithm

# Input 1: array - an array where the elements have been sorted in ascending order
# Input 2: target - the number that we are searching for
# Returns: the index of target in the array
import math

def binarySearch(array, target):
    lower = 0
    upper = len(array)-1
    while(lower != upper):
        middle = math.ceil((lower + upper)/2)
        if array[middle] > target:
            upper = middle - 1
        else:
            lower = middle
    if array[lower] == target:
        return lower
    else:
        return -1

def demonstrate():
    testArray1 = [1,2,3,5,8,9,100,356,478]
    target1 = 8
    result1 = binarySearch(testArray1, target1)
    print(result1)

    testArray2 = [33, 45, 67]
    target2 = 77
    result2 = binarySearch(testArray2, target2)
    print(result2)

    testArray3 = [-19, -2, 0, 3, 45, 619003]
    target3 = 0
    result3 = binarySearch(testArray3, target3)
    print(result3)

demonstrate()
