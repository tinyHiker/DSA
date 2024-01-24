class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 


class InsertionError(Exception):
    def __init__(self, message, extra_info=None):
        super().__init__(message)
        self.extra_info = extra_info

    def get_details(self):
        return f"Additional Information: {self.extra_info}"
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length +=1

    def __str__(self):
        next_node = self.head
        print_string = ""
        while next_node != None:
            print_string += str(next_node.value) + " -> "
            next_node = next_node.next

        return print_string

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index > (self.length - 1):
            raise InsertionError("Index {index} does not exist")
        elif index < 0:
            raise InsertionError(f"Cannot use negative index: {index}")
        elif index == 0:
            new_node.next = self.head 
            self.head = new_node
        else: 
            temp_node = self.head 
            for i in range(index-1):
                temp_node = temp_node.next 
                new_node.next = temp_node.next
                temp_node.next = new_node
        self.length += 1 
        

    def traverse(self):
        current = self.head 
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head 
        index = 0
        while current is not None:
            if current.value == target:
                return index
            index += 1
            current = current.next 
        return -1
    
    def get(self, index):
        current = self.head 
        for i in range(index):
            current = current.next
        return current.value
    
    def get_node(self, index):
        current = self.head 
        for i in range(index):
            current = current.next
        return current
    

        
    
    def set_value(self, index, value):
        current = self.head 
        for i in range(index):
            current = current.next
        current.value = value

    def pop_first(self):
        
        value = self.head.value
        store = self.head
        self.head = self.head.next
        store.next = None

        if self.length == 1:
            self.tail = None
        
        self.length -= 1

        return value
    
    def pop(self):
        value = self.tail.value
        current = self.head
        while current.next is not self.tail:
            current = current.next
        current.next = None 
        return value
    
    def remove(self, index):
        value = None
        if index == 0:
            value = self.pop_first()
        elif index + 1 == self.length:
            value = self.pop()
        else:
            prev_node = self.get_node(index-1)
            cur_node = self.get_node(index)
            next_node = self.get_node(index+1)
            prev_node.next = next_node
            cur_node.next = None 
            self.length -= 1
            value = cur_node.value

        return value 



    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
print(new_linked_list)
new_linked_list.pop()
print(new_linked_list)
            

