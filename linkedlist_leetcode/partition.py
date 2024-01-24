from sample_list import LinkedList

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