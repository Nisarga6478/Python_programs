#Question 5:Write a python program to print list is empty or not.
def great(list1):
    if len(list1)==0:
        return 0
    else:
        return 1
list1=[]
# list1=[1,3,5,7,8]
if great(list1):
    print("not empty")
else:
    print("empty")

#Question :Program of list using for loops.
list1=[]
for i in range(int(input('Enter range:'))):
    list1.append(i)
print(list1[1:10])

list2=[x for x in range(int(input("enter starting range")),int(input("enter last range")))]
print(list2)
del list2[0]
print(len(list2))
print(list2[::-1])
print(list2[1:0])

list3='hle2l3l4o5w6o7r8l9d'
print(list3[0],list3[2],list3[1],list3[4],list3[8],list3[10],list3[12],list3[14],list3[1],list3[-1])

