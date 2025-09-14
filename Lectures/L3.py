# String mainipulation

# a= "Hello World"
# print(len(a))  # Output: 11
# print(a.count('o'))  # Output: 2
# print(a.upper())  # Output: "HELLO WORLD"
# print(a.lower())  # Output: "hello world"
# print(a.index('o'))   # Output: 4
# # print(a.index('o' , 15,34))   # Output: 4 --> we cwn provide the range also to know the index.
# print(a.capitalize())  # Output: "Hello world"
# print(a.casefold())  # Output: "hello world"--> changes all characters to lowercase
# print(a.find("o"))  # Output: 4
# print(a.find("o",15,34,))  # Output: 4 --> we cwn provide the range also to know the index.

# print(name.isalnum())  # Output: True --> checks if all characters are alphanumeric.
# print(name.isalpha())  # Output: True --> checks if all characters are alphabetic
# print(name.isdigit())  # Output: False --> checks if all characters are digits.
# print(name.islower())  # Output: True --> checks if all characters are lowercase.
# print(name.isupper())  # Output: False --> checks if all characters are uppercase.
# print(name.isspace())  # Output: False --> checks if all characters are whitespace.
# print(name.isnumeric())  # Output: False --> checks if all characters are numeric.

# name="john"
# a="My name is {}"
# print(a.format(name))  # Output: "My name is john"
# print(a.format("Alice"))  # Output: "My name is Alice"
# print(name.center(10, '*'))  # Output: "**john*****"
# print(name.ljust(10, '*'))  # Output: "john******"
# print(name.rjust(10, '*'))  # Output: "*****john"
# print(name.replace('o', 'a'))  # Output: "jahn"  
# a= "Hello World"
# print(a.rindex('o'))  # Output: 7
# print(a.rindex('o',5.8))  # Output: 7  --> we cwn provide the range also to know the index.
# print(a.rfind('o'))  # Output: 7
# print(a.rfind('o',6,14))  # Output: 7 --> we cwn provide the range also to know the index.
# print(a.split())  # Output: ['Hello', 'World']
 

# string sicing:-
# a= "Harry potter and the gobleyt of fire."
# b="0123456789"
# print(a)
# print(a[0:5]) / print(a[:5]) # Output: "Hello" --> from index 0 to index 4. 
# print(a[6:11])  # Output: "World"
# print(a[-4:])  # Output: "fire." --> from index -4 to end.
# print(a[6:11:2])  # Output: "Wr" --> from index 6 to index 10 with a step of 2.  
# print(b[::2]) # Output: "02468" --> from index 0 to end with a step of 2.
# print(b[::-1]) # Output: "9876543210" --> reverse the string.
# print(b[:7:2]) # Output: "0246" --> from index 0 to index 6 with a step of 2.
# print(b[7:]) # Output: "789" --> from index 7 to end
# print(b[6:0:-1])/ print(b[6::-1]) # Output: "6543210" --> from index 6 to index 0 in reverse order.

# LISTS:-

# fruits=["apple","mango","banana" ,12,14,45.10]
# print(fruits)  --> ['apple', 'mango', 'banana', 12, 14, 45.1]
# print(type(fruits))  ---> <class 'list'> 

# Slicing of list:-

# a=["Ironman","Thor","Captain America", "Hulk"]
# those properties that we use in string , will be same used in list also. 
# Note:- from left onwards the index starts from "0" and from right the index starts from "-1".
# print(a[1]) ---> output:- Thor
# print(a[1:3]) ----> output:- ['Thor', 'Captain America']
# print(a[0:2]) ---> output:- ['Ironman', 'Thor']
# print(a[:2]) ---> output:- ['Ironman', 'Thor']
# print(a[1:]) ----> output:- ['Thor', 'Captain America', 'Hulk']
# print(a[1:4]) ----> output:- ['Thor', 'Captain America', 'Hulk']
# print(a[1:]) ----> output:- ['Thor', 'Captain America', 'Hulk']
# print(a[::2]) ----> output:- ['Ironman', 'Captain America']
# Note:- we put [::]  , to mark that we do not specify starting variable and ending variable , first space is of starting variable and second space is for ending variable 
# Note:- print(a[::2]) ---> in this type , we specify no starting and ending variable but , the third space we specified is for the no. of iteration. for ex:- in this case it is 2.
# print(a[-3:-1]) ----> output:- ['Thor', 'Captain America']
# print(a[::-1]) ----> output:- ['Hulk', 'Captain America', 'Thor', 'Ironman']
# print(a[-1:-4:-1]) ----> output:- ['Hulk', 'Captain America', 'Thor']


# String Iteration:=

# a= ["Hulk","Thor","ironman","captain america"]

# 1. Iteration using For Loop:-
# for i in a:
#     print (i)

# using for loop with range and length function
# for i in  range(len(a)):
#     print(a[i])

# using while loop
# i=0
# while i<(len(a)):
#     print(a[i])
#     i+=1

# using short- hand for loop
# [print(i) for i in a ]


# Functions in List:- (PART - 1)
# a= ["Thor","Hulk","ironman","captain america","Hulk"]
# print(a)

# find the length 
# print(len(a))

# count an occurence of a particular element
# print(a.count("Thor"))

# to add to the list  --> it will add the element in the last from all the element
# a.append("spiderman")
# print(a) 

# to add to a specific location --> it will add the element in the at any position
# a.insert(1,"vision")
# print (a)

# to remove from a list
# a.remove("Hulk")
# a.remove("spiderman")
# print(a)

# to remove from a certain location 
# print (a.pop(1)) --> here , we provide index number of the element that needs to be removed
# print(a)

# Functions in List:- (PART - 2)
# a= ["Thor","Hulk","ironman","captain america"]


# to create a copy of a list
# b=a.copy()
# print(b) ---> ['Thor', 'Hulk', 'ironman', 'captain america']

# to access an element
# print(a.index("Thor")) --> 0

# to extend the list
# c=["vision","spiderman"]
# a.extend(c)
# print(a)  ---> ['Thor', 'Hulk', 'ironman', 'captain america', 'vision', 'spiderman']

# to reverse the list
# a.reverse()
# print(a) ---> ['captain america', 'ironman', 'Hulk', 'Thor']

# to sort the list
# a.sort()
# print(a) ---> ['Hulk', 'Thor', 'captain america', 'ironman']
# d=[1,7,5,9,10,2]
# d.sort()
# print(d) ---> [1, 2, 5, 7, 9, 10]

# to clear all the data from the list
# a.clear()
# print(a) --> []
# d.clear()
# print(d) --> []


# list comprehension:-

# l1=[30,40,50,60]

# l2=[]
# for i in l1:
#     l2.append(i)

# print(l1, "\n" , l2)  ----> [30, 40, 50, 60] 
#                             [30, 40, 50, 60]
  
#   or

# l1=[30,40,50,60]

# l2=[]
# for i in l1:
#     if i> 45:
#         l2.append(i)

# print(l1, "\n" , l2)  ---> [30, 40, 50, 60] 
#                             [50, 60]

# instead of these all things we can simply make list comprehension

# l3=[i for i in l1]
# print(l3) ---> [30, 40, 50, 60]

# l3=[i for i in l1 if i>45]
# print(l3)  ----> [50, 60]

# we use list comprehension in that time only , when we have to copy data of list to data of another list 



