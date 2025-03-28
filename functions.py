#default parameter
def student_info(s_name,batch_name="37r",inst_name="10000 coders"):
    print(s_name+batch_name+inst_name)
student_info("sandhya")
student_info("sandeep")
student_info("radha")

#keyword parameter
def sample(b,a):
    print(a,b)
sample(a=4,b=5)

#positional arguements
def nameage(name,age):
    print("hi,i am",name)
    print("my age is",age)
nameage(name="sandhya",age=20)

#combining positional and keyeord parameter
def sample(a,b,/,*,c,d):
    print(a+b+c+d)
sample(2,4,c=5,d=6)

#arbitary arguements
def my_function(*kids):
    print("the youngest child is"+kids[2])
my_function ("sandhya","sandeep","reddy")

#return function
def sample():
    print("hello world")
    return("execution completed")
print(sample())

#lambda function
f_class=lambda x:"hello"+x
print(f_class("sandhya"))

#research about combining positional and key word parameter
#Explanation of / and *
 #  (Positional-Only Arguments):
 #  The / symbol in a function's parameter list indicates that all parameters before it must be passed as positional arguments.
 #  This means you cannot use their names to pass them as keyword arguments.
 #   Keyword-Only Arguments):
 #  The * symbol in a function's parameter list indicates that all parameters after it must be passed as keyword arguments.
 #  This means you must use their names to pass them, and you cannot pass them positionally.

 #research about pass by value and pass by reference

 # When passing variables to a function, there are two ways a language can handle it:
 # Pass by Value – The function gets a copy of the variable. Changes inside the function do not affect the original variable.
 # Pass by Reference – The function gets a reference to the original variable. Changes inside the function affect the original variable