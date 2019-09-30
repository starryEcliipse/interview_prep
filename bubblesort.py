# This is my implementation of bubblesort sorting algorithm

def bubblesort(Array):
    count = 0
    while count == 0:
        swapped = False
        for index in range(len(Array)-1):
            count = count + 1
            if Array[index] > Array[index+1]:
                temp = Array[index]
                Array[index] = Array[index+1]
                Array[index+1] = temp
                swapped = True

        if swapped == True:
            count = 0


    return Array

def demonstrate():
    testArray = [35,5,1,7]
    testOutput = bubblesort(testArray)
    print(testOutput)

    testArray2 = [333, 40, -7, -7, 800, 2, 1, 3]
    testOutput2 = bubblesort(testArray2)
    print(testOutput2)

demonstrate()
