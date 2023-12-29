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
    

    
def remove_duplicates(ll: LinkedList):
    '''Removes duplicate elements from a sorted LinkedList'''
    current = ll.head
    
    if ll.head is None:
        return ll
    
    while current.next is not None:
        if current.value == current.next.value:
            if current.next == ll.tail:
                current.next = current.next.next
                ll.tail = current
                break
            else:
                current.next = current.next.next
        else: 
            current = current.next
    
    return ll
            

def kth_last(ll: LinkedList, k: int):
    if k > len(ll) - 1 or k < 0:
        return None
    
    pos = len(ll) - k  
    
    current = ll.head
    for _ in range(pos):
        current = current.next 
        
    return current


def partition(ll: LinkedList, target: int):
    current = ll.head
    i = 0
    while current.next:
        if current.next.value < target:
            if current.next == ll.tail:
                ll.tail = current
                store = current.next
                current.next = current.next.next
                store.next = ll.head
                ll.head = store 
            else:
                store = current.next
                current.next = current.next.next
                store.next = ll.head
                ll.head = store
 
        else:
            current = current.next

    return ll

def sum_lists(ll_1: LinkedList, ll_2: LinkedList):
    num_str_1 = ""
    num_str_2 = ""
    
    current = ll_1.head
    while current:
        num_str_1 = str(current.value) + num_str_1
        current = current.next
        
    current = ll_2.head 
    while current:
        num_str_2 = str(current.value) + num_str_2
        current = current.next
        
    return int(num_str_1) + int(num_str_2)


        


l2 = LinkedList()
l2.add(100)
l2.add(1)
l2.add(200)
l2.add(2)
l2.add(300)
l2.add(3)

print(l2)
partition(l2, 4)
print(l2)



        