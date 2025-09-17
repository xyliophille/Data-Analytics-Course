# defining the function:-

# def hello():
#     print ("hello world")

# calling the function:-

# hello()    ---> output:- hello world

# def add():
#     x=56
#     y=23
#     print (x+y)
# add()    

# parameters and arguments in function

# parameters- these are the vsaribles written inside the the parantheses with the name of function.

# Arguments- These are the values passed to the parameers eile calling the function.

# def add (x,y):
#     print (x+y)

# add (12,67) ---> 79

# Ex:- 

# def area(length , breadth):
#   print ("the area of the rectangle is:", length * breadth)

# area(12,56)

# original version:-
# def hello(name):
#   print("hello ,my name is", name)

# hello("ayush")

# on converting it in arbitrary argument:- representing in the form of tuple, and accessing it using  by providing index number.
# def hello(*name):
#   print("hello ,my name is", name[0])

# hello("ayush","lisa","aman")

# return statement is used to exit a function and return the value of the function.

# def hello():
#     return("hello")

# print(hello()) ---> hello   
# (hello()) ---> no output

# def add(a,b):
#     return(a+b)

# print (add(12,4)) ---> 16     

# Recursion in python:-

# It is most commonly used mathematical and programming concept.
#  In simple words, recusrion means a function can call iteself, giving us a benefit of looping through data in order to get a result.

# print (add(12,4)):

# def hello():
#     print("hello")
#     return hello()

# print (hello()) -----> it will stop executing until the limit of the python id reached, here it is 995 words.

# def fact(n): (factorial of n numbers)
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)


# print(fact(5)) ---> 120
