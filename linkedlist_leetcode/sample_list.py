
from random import randint 

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None 
        
    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current = self.head 
        while current:
            yield current
            current = current.next 
            
    def __str__(self):
        elems = [str(x.value) for x in self]
        return ' -> '.join(elems)
    
    def __len__(self):
        result = 0
        node = self.head 
        
        while node:
            result += 1
            node = node.next 
            
        return result
    
    def add(self, value):
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        return self.tail 
    
            
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self