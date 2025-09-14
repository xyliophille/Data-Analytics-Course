#for loop:=
# for i in range (2,6,2)/(2,6):
# here (2,6,2)--> this means that at last 2 , it is used to define the number of iteration.
#      print(i)    
# multiplicatiion table of 7 : 
# n=7   /  n= int(input("enter a  number:"))
# for i in range (1,11)
#   print (n,"x",i,"=", n*i)


#while loop:=
# n=1
# while n<=5:
#     print (n)
#     n+=1

# multiplicatiion table of 7 : 
# n=1
# a=7/ a= int(input("enter a  number"))
# while n<=10:
#     print(a,"x",n,"=",n*a)
#     n+=1


#while true loop:=----> it is (returns) actually a infnite loop
# n=1
# while True:
#     print(n)
#     n+=1

# while True:
#     num1= int(input("enter a number:"))
#     num2= int(input("enter a number:"))

#     print(num1+num2)
#     repeat = input("o yu want to end the program") ----> ask everytime to end the program
#     if repeat== "yes":
#         break

#nested loop:=
# for i in range (1,4):
#     for j in range (1,11):
#         print(j) /// print(j,end ="")
#     print()  
# Note:print(j,end ="")---> it is used to align the one loop content in one single line
# Note:Outer loop is used to count the no. of rows and inner loop is used to count the no. of columns, in pattern type problems. 

# Q. pattern - 1
#              12
#              123
#              1234 
#              12345

# for i in range (1.6):
#   for j in range (1,i+1):
#       print(j,end=" ")  
#   print()

# loop with conditional statements
#  for i in range (1,101):
#      if i%8 ==0 and i%12==0:
#         print (i)

# n=1

# while n<=10:
#   if n==3:
#       print("yes")
#   else:
#       print("n")
#   n+=1


# Break and continue
# continue:=
#  for i in range (1,11):
#     if i==5:
#        continue  // it will skip 5
#       else:
#          print(i)
    
#  Break:=
# for i in range (1,11):
#     if i==7:
#        break  // it will skip (will not execute) all the numbers from 7 till end.
#       else:
#          print(i)

# print("thank you")
# a=135.13
# print(float(a))

# print(int(a))
# print(type(a))
