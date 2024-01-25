from sample_list import LinkedList

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