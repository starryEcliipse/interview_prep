# Write a function to determine whether stringB is a substring of stringA

def isSubstring(stringA, stringB):
    counter = 0
    print(len(stringB))
    for charA in stringA:
        for charB in stringB:
            if charA == charB:
                counter = counter + 1
    if counter == len(stringB):
        return True
    return False

testA = "hello"
testB = "world"

print(isSubstring(testA, testB))

testB2 = "he"
print(isSubstring(testA, testB2))
