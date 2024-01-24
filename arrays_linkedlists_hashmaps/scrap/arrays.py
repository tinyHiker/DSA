from array import *

# 1. Create an array and traverse
print("Step 1")
my_array = array('i', [1,2,3,4,5])

for i in my_array:
    print(i)
   
   
# 2. Access individual elements through indexes 
print("Step 2")
print(my_array[0])

# 3. Append any value to the array using append method
print("Step 3")
my_array.append(6)  # O(1)
print(my_array)


# 4. Insert value in an array using insert() method
print("Step 4")
my_array.insert(3, 11)
print(my_array)

# 5. Extend python array using extend() method 
print("Step 5")
my_array1 = array('i', [10, 11, 12])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist()) method
print("Step 6")
tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any array element using remove() method
print("Step 7")
my_array.remove(11)  # only removes the first occurence of 11
print(my_array)

# 8. Remove last array element using pop() method
print("Step 8")
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using the index() method
print("Step 9")
print(my_array.index(21))

# 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print("Step 11")
my_array.buffer_info()

# 12. Check for number of occurences of an element using count() method
print("Step 12")
my_array.append(11)
print(my_array.count(11))
print(my_array)

# 14. Convert array ot a python list with same elements using tolist() method
print("Step 14")
print(my_array.tolist())


# Two Dimensional Arrays
print("Two Dimensional Arrays")

#Table 1 - Daily Temperatures for each Day
# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np 
twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5], 
                      [12, 17, 12, 8], 
                      [15, 18, 14, 9]])

print("Before insert")
print(twoDArray)


print("After insert")
newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis = 0) # axis = 0 means insert as a row
# axis = 1 means insert as a column
print(newTwoDArray)


#There's also np.append where you don;t have to specifcy the index you want to isert at