# This is my solution to the super reduced string problem on hacker rank
# https://bit.ly/2tuzd3E

def reduceString(inputString):
    Array = list(inputString)
    while True:
        Array, shouldContinue = deleteChar(Array)
        if shouldContinue == True:
            deleteChar(Array)
        else:
            break
    if len(Array) == 0:
        return "Empty String"
    else:
        outputString = ''.join(Array)
        return outputString

def deleteChar(Array):
    for index in range(len(Array)-1):
        if Array[index] == Array[index+1]:
            Array.pop(index+1)
            Array.pop(index)
            return Array, True
    return Array, False


def demonstrate():
    testString1 = "aaabccddd"
    testOutput1 = reduceString(testString1)
    print(testOutput1)

    testString2 = "aa"
    testOutput2 = reduceString(testString2)
    print(testOutput2)

    testString3 = "baab"
    testOutput3 = reduceString(testString3)
    print(testOutput3)

demonstrate()
