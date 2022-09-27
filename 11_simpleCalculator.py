def calc(a,b,operator):
         # parameters
    if(operator=="+"):
        return a+b
    elif(operator=="-"):
        return a-b
    elif(operator=="*"):
        return a*b
    else:
        return a/b

# a=5
# b=9
# operator=*

# *==* #is eaual to

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
operator= input("Enter operator (+,-,*,/):")
print("Calculating....")

print("Answer:",calc(a,b,operator))

