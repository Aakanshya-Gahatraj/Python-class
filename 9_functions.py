# function: a block of code that performs a specific task
# Without function, when writing huge code of lines it becomes difficult to know what a specific code is for
# With function, we can reuse the same piece of code for same operation eg;

# Students Marks Calculation:

# Ram- total score: 400 out of 500
# Shyam- total score: 200 out of 500
# Ravi- total score: 300 out of 500

# print("Ram percentage: ", 400/500*100)
# print("Shyam percentage: ", 200/500*100)
# print("Ravi percentage: ", 300/500*100)

#                           this is called parameter¬
def percent_calculation(student_name, achieved_marks, total_marks):
    print(student_name, "percentage:", achieved_marks/total_marks*100)

#                    these value that we pass in function is called arguement
percent_calculation("Ram",400,500) 
percent_calculation("Shyam",200,500)
percent_calculation("Ravi",300,500)

# this is a default parameter
def greeting(name="new person"):
    print("Hello "+name)

greeting("Tom")
greeting()


# User-defined Function:  Functions that user makes like percent_calculation() function above.
# Built in function: Already present in python eg; print(), input(), str(), sort(), sum()
# sum() function only works with list

list=[2,3,5]
print(sum(list))