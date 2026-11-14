from collections import Counter
class MinStack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = Counter()

    def push(self, val: int) -> None:
        self.counter.update([val])
        if self.head is None:
            self.head = self.tail = Node(val, None, None)
        else: 
            temp = Node(val, self.tail, None)
            self.tail.next = temp
            self.tail = temp

    def pop(self) -> None:
        if self.head is None: raise ValueError("Array empty")
        self.counter -= Counter([self.tail.data])
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def top(self) -> int:
        return self.tail.data

    def getMin(self) -> int:
        return min(self.counter)
        

class Node:
    def __init__(self, value, prev, next):
        self.data = value
        self.prev = prev
        self.next = next