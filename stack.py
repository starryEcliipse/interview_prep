# Implementation of the stack data structure
# Source: https://docs.python.org/3.1/tutorial/datastructures.html

class Stack:

    def __init__(self):
        self.array = []


    def push(self, item):
        #Adds an item to the Stack
        self.array.append(item)

    def pop(self):
        #Removes and returns an item from the Stack
        return self.array.pop()

    def size(self):
        #Returns the size of the stack
        return len(self.array)

    def peek(self):
        #Returns the next item in the stack but does not remove it
        last = self.array[len(self.array)-1]
        return last

    def isEmpty(self):
        if(len(self.array)) == 0:
            return True
        return False
