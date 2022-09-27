# Sometimes, we want to perform a task more than once. In such case we use loops.
# While and for loop in python:

'''In while loop, condition is checked first. If the condition is met,
while loop is executed.
else, not executed! 
While loop will keep on looping until the given condition is satisfied.
'''
# a=0
# while (a<5):
#     print("Hello World!")

b=1
while (b<=5):
    print(b)
    b+=1

animals= ["Monkey","Dog","Shark","Cheeta"]
i=0
while(i<len(animals)):
    print(animals[i])
    i+=1

# in keyword: to iterate, to check value in list or string
if("Dog"in animals): 
    print("\nYes!!\n")

for animal in animals:
    print(animal)

z=0
for z in range(1,10):
    if(z==2):
        pass # Do Nothing!!
    if(z==5):
        print("Not Printing 5")
        continue
    elif (z==7):
        break
    else:
        print(z)
