# Implementation of the queue data structure

class Queue:

    def __init__(self):
        self.array = []

    def enqueue(self, item):
        self.array.insert(0, item)


    def dequeue(self):
        return self.array.pop()
