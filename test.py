mylist=[0,5,2,1]
print(mylist)
mylist.sort()
print(mylist)

num=[11,2,3,1,5,6]
# ix= 0,1,2,3,4,5
num.insert(5,20) #insert 20 in 5th index
print("Insert 20 at index 5:",num)
num.pop()
print("Pop:",num) 
num.pop(2)
print("Pop at index 2:",num)
num.remove(11)
num.remove(2)
num.remove(5)
print("Remove :",num)
