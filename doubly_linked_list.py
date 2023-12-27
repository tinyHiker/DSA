class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.prev = None

    def __str__(self):
        return str(self.value)
    
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None: 
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node 
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        if self.head is None:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node 
            self.length += 1
        
    

    def __str__(self):
        temp_node = self.head 
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next 
        return result



dll = DoublyLinkedList()
dll.append(1)
dll.append("Taha")
dll.prepend("Iqbal")

print(dll)
print(dll.length)