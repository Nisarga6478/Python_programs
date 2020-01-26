# Question  3:Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
# For example: List = [54, 44, 27, 79, 91, 41]
# Expected Output:
# Original list  [34, 54, 67, 89, 11, 43, 94]
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
a1= [54, 44, 27, 79, 91, 41]
del a1[4]
print(a1)
a1.insert(2,100)
print(a1)
a2=[34, 54, 67, 89, 11, 43, 94]
print(a2)
del a2[4]
print(a2)
a2.insert(2,11)
print(a2)
a2.append(11)
print(a2)

#Question 4:Write a Python program to find the second largest number in a list.
l1= [4, 3, 0, 7]
l1.sort()
print("second largest number",l1[-2])

#Question 5:Write a python program to print list is empty or not.

def great(list1):
    if len(list1)==0:
        return 0
    else:
        return 1
# list1=[]
list1=[1,3,5,7,7]
if great(list1):
    print("not empty")
else:
    print("empty")
