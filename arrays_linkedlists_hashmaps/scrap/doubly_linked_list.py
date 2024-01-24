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
            
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
    
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            
    def search(self, target):
        current = self.head 
        while current is not None:
            if current.value == target:
                return True
            current_node = current.next
        return False        
    
    def get(self, index):
        if index < self.length // 2:
            current_node = self.head 
            for _ in range(index):
                currrent_node = current_node.value
        else:
            current_node = self.tail
            for _ in range(self.length-1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set_value(self, index, value):
        node = self.get(index)
        if node: 
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of bounds.")
            return
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return 
        elif index == self.length:
            self.append(value)
            return 
        
        prev = self.get(index - 1)
        n_cur = self.get(index)
        new_node = Node(value)
        new_node.prev = prev
        prev.next = new_node
        new_node.next = n_cur
        n_cur.prev = new_node 
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
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

dll.insert(2, "Taha")
print(dll)