from sample_list import LinkedList 

def sum_lists(ll_1: LinkedList, ll_2: LinkedList):
    "Sums the elements of two lists of equal length"
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