# List: A container to store values of different data types. List is mutable.
# Indexing same like string. Starts from 0 index.

# List= []
# Tuple= ()

print("\n")
a=[1,2,3,True,"End"]
print(a)

my_list=[1,2,3]
my_list2=[1,2,3,"string",True]
#         0 1 2  3        4
my_list2[3]=7

a[0]="Start"
print(a)

# List Slicing
names= ["Tom","Jerry","Marry","Jane"]
#index=   0      1       2       3

print(names[::-1]) #reverses
print(names[1:3]) # excludes 3rd index

# List Functions
# These functions change the original list.
 
num=[6,2,3,1,8,0]
print("\nOriginal:",num)
num.sort()
print("Sorted:",num)
num.reverse()
print("Reverse:",num)
num.append(45)
print("Append 45:",num)
num.insert(5,20) #insert 20 in 5th index
print("Insert 20 at index 5:",num)
num.pop()
print("Pop:",num) # removes last number
num.pop(2)
print("Pop at index 2:",num)
num.remove(0)
print("Remove :",num)


# Tuple: immutable data-type in python that stores different datatypes.

t1= (1,2,3)
# t1[0]=0 #is immutable
print(t1)

# declaring tuple
t2= ()
print(t2)

# t3=(1) # Not a tuple
t3=(1,)
print(type(t3))

t=(1,"apple",5,True)
print(t)

t4= (1,2,1,1)
print(t4)

#Tuple methods:
print(t4.count(1))
print(t4.index(2))