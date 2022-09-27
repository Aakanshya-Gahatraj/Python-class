f_name="Iron "
l_name="Man"

print(f_name+l_name) #  Concatenation
print(f_name * 3) # Repeat a string
print(f_name[2]) #  Printing character in an Index

# f_name[0]="a" #String is immutable
# print(f_name)

# Slicing
fruit= "apple"
print(1,fruit[0:3]) # excluding 3rd index
print(2,fruit[:3])
print(3,fruit[0:])
print(4,fruit[:])
print(5,fruit[-5:-1])
print(6,fruit[::3]) # skip 
print(7,fruit[::-1]) # reverses the string 
word="educations"
print(0, word[::1] )
print(0, word[::-1] )
print(0, word[::-2] )

# Other functions
name= "Hello how are you? My name is Tom. Its nice to meet you."
#inde= 01234567891011



print("\nLength of string name is:",len(name))
print(name.find("you")) #index of first occurence of you
print(name.replace("Tom","Jerry"))
