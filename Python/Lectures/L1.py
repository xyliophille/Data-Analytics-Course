# printing the results in just single line
# print("Hello World")
# print("This is my first Python program")
# print("I am learning Python programming.")

# printing the results in multiple lines
# Method 1:-
# print(""" Hello World
# This is my first Python program
# I am learning Python programming.""")
# Method 2:-
# print("hello myself \nhello universe.")
# special case:-
# print('it's my name ')  --> there is error came in applying apostrophie, therefore to hide this error we use print('it\s my name') code.

# single line comment- # code
# multiple line comment- """.......code......."""

#  variable is a container that holds data inqside it as a value.
# Ex:- a=" hello" 
# print(a)  --> output  :- hello
# print("a")  --> output  :- a

#   Name = "john"
# print (name)   --> output gives  error
# Even num = 2  --> output gives  error
# EvenNum=2 --> output does not  gives  error
# Even_num=2 --> output does not  gives  error
# variable always start with the letters only, not with number or special characters.

# name = str(input("Enter your name here"))
# print(name)
# name = int(input("Enter your no. here"))
# print(name)
# name = float(input("Enter your name here"))
# print(name)
# solve = eval(input("Enter your equation here"))
# print(solve)   --->   print("hello world")- hello world  ,   5*6=30

# Typecasting:-
# 1.Implicit typecasting- where python itself converts one datatype to another.
# 2.Explicit typecasting- where the user converts one datatype to another.  

# name = "ayush"
# age= 23
# print(type(name)) ----> output :- <class 'str'>

# implicit example-
# a=123
# b=1.23
# print(type(a))
# print(type(b))

# c= a+b
# print(c)
# print(type(c))

# -- output:-  
# <class 'int'>
# <class 'float'>
# 124.23
# <class 'float'>

# Explicit conversion
# a=123
# b=1.23
# print(type(a))
# print(type(b))

# a= int(a)
# print("after conversion", type(a))

# c= a+b
# print(c)
# print(type(c))

# # output:-
# <class 'int'>
# <class 'float'>
# after conversion <class 'int'>
# 124.23
# <class 'float'>

#  note:- a,b=b,a  that means left,right=right ,left , that means value of a will become value of b and value of b beomes value of a.
  
# floor divison- //
# ex:- print(8//3) --> 2

# power :- **
# print(2**10)--> 1024

# comparison operators:-
# print(3>6) 
#  == ---> tells whether both values are equal or not?


# logical operators  ---.  and , or , not -- >  its output is (returns) always in true pr false.
# and- tells if both the operands are true.
# or- true if either of the operands is true  
# not- give complement of the the input either true or false.
#  print(3>4 or 3<4)
#  print(3>4 and 3<4)
#  print(not(3>4 and 3<4))

# assignment operators:- used to assign values 
#  ex:- =, +=, -= , *=.

# identity operators:- tells whether both the data types are same or not.  its type is Is and Is not . ouptput is either true or false.
# for ex:- a= 1234
#           b= "1234" / b= 1234
#           print(a is b) ---> output:- false  --> a is equal to b
#           print(a is not b) ---> output:- true --> a is not equal to b

#  bitwise operator:- and(&),or(|),xor(^), <<(zero fill left shift) ,>>(zero fill right shift)

# finding binary numbers:- print (bin(10))---> output:- 1010

# for ex:- 
# a=10 --> 1010
# b= 8 -->1000
# print (a & b)  ////   print (a | b)  print (a ^^ b)
#  --> output :- 1000-> 8
# same as with or operation.

# zero fill left shift:- for ex:= 10= 1010
#  our question is 10<<2 (zero fill left shift), then it will delete 2 digit from left and put 2 zeros in left most of the number . 
# therefore , our final value of 10<<2 is  0010--> 2.
# same as with 10<<1 , then the final value is 0101 , by deleting ne zeros from left side  
#  for ex:= print(10<<2)---> output is = 2. 

# zero fill right shift:- for ex:= 1010 , then on right shift of (10>>1) it will add one zero at end , and tell the final result as 10100---> 20.
#  same as with 10==1010, 10>>2 , then output is 40 (101000) by putting 2 zeros at end.
#  for ex:= print(10>>2)---> output is = 40. 

# membership operators:= 
# tells wheteher(whether it is member of it or not) that letter/word is present in that full word / sentence or not?
# types:= 1. in
#         2. not in

# for ex:= a="hello"
# print("e" in a )--> true
# print("e" not in a )--> false
# print("p" not in a )--> true

# 1. if statement:=
# marks = 87

# if marks>=90:
#     print("you will get")

# print("thank you")    


# shorthand of if statemnt- 
# marks=87
# if marks>=90: print ("yes")

# 2. if-else statement:=
# marks=87

# if marks>=90:
#     print("yes")
# else:
#     print("no")

# print("thank you")

# shorthand of if-else statemnt- 
# marks= 97
# print("tes") if marks>=90 else print ("no")



# 3. if-elif-else statement:=
# marks=87

# if marks>=90:
#     print("yes")
# elif marks >=80 and marks <=90:
#     print("yup")  
# elif marks >=70 and marks <=80:
#     print("hello")  
# else:
#     print("no")

# 4.Nested if statement:=
# marks=87

# if marks>=90:
#     print("yes")
#     if marks>=95:
#         print("hello")
# else:
#     print("no")  




