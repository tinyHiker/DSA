"""Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:

False
"""


def check_same_frequency(list1, list2):
    
    dict_1 = dict()
    dict_2 = dict()
    
    
    for e in list1:
        dict_1[e] = dict_1.get(e, 0) + 1 
        
    for e in list2:
        dict_2[e] = dict_2.get(e, 0) + 1 
        
    return dict_1 == dict_2

