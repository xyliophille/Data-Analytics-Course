# tuples:-

# a= ("oneplus, samsung, apple, vivo, oppo")
# print(a[1,3])  # Output: "samsung, apple" --> from index 1 to index 2.
# print(a[:3])  # Output: "oneplus, samsung, apple" --> from index 0 to index 2.
# print(a[2:])  # Output: "apple, vivo, oppo" --> from index 2 to end.
# print(a[1::2])  # Output: "samsung, vivo" --> from index 1 to end with a step of 2.
# print(a[::-1])  # Output: "oppo, vivo, apple, samsung, oneplus" --> reverse the tuple.
# print(a[2::-1])  # Output: "apple, samsung, oneplus" --> from index 2 to end in reverse order.

# # WITH FOR LOOP:-
# 1.for i in a:
#     print(i)  # Output: "oneplus, samsung, apple, vivo, oppo" --> prints each element of the tuple.
# 4
# #along with range and length in for loop:- 

# 2.for i in range(len(a)):
#     print(a[i])  # Output: "oneplus, samsung, apple, vivo, oppo" --> prints each element of the tuple using index.

# 3. by while loop:
# i = 0
# while i < len(a):
#     print(a[i])  # Output: "oneplus, samsung, apple, vivo, oppo" --> prints each element of the tuple using index.
#     i += 1

# # TUPLES:-

# a= "apple", "mango", "banana", 1,67,1.23
# print(type(a))  # Output: <class 'tuple'> --> confirms that 'a'
# print(a)  # Output: ('apple', 'mango', 'banana', 1, 67, 1.23) --> tuple with mixed data types.
# # a.append("orange")  # This will raise an (Attribute) Error because tuples are immutable.
# a.add("kiwi")  # This will also raise an (Attribute) Error because tuples do not have an 'add' method.
# print(a)  # This line will not be executed due to the previous errors.


# a=("oneplus", "vivo", "redmi", "samsung", "Nokia")
# print(a[1:3])  # Output: ('vivo', 'redmi') --> from index 1 to index 2.
# print(a[:3])  # Output: ('oneplus', 'vivo', 'redmi') --> from index 0 to index 2.
# print(a[2:])  # Output: ('redmi', 'samsung', 'Nokia') --> from index 2 to end.
# print(a[1::2])  # Output: ('vivo', 'samsung') --> from index 1 to end with a step of 2.
# print(a[::2])  # Output: ('oneplus', 'redmi', 'Nokia') --> from index 0 to end with a step of 2.
# print(a[::-1])  # Output: ('Nokia', 'samsung', 'redmi', 'vivo', 'onreplus') --> reverse the tuple.
# print(a[2::-1])  # Output: ('redmi', 'vivo', 'oneplus') --> from index 2 to end in reverse order.



# a=("oneplus", "vivo", "redmi", "samsung", "Nokia")
# with for loop:-
# for i in a:
#     print(i)  # Output: prints each element of the tuple.   

# along with range and length in for loop:-
# for i in range(len(a)):
#     print(a[i])  # Output: prints each element of the tuple (using index).

#along with while loop:-
# i = 0
# while i < len(a):
#     print(a[i])  # Output: prints each element of the tuple (using index).
#     i += 1



# Converting tuple to list and vice versa: 

# a= ("oneplus", "samsung", "apple", "vivo", "oppo")
# print("before conversion:", type(a)) // Output: before conversion: <class 'tuple'>

# a=list(a)  # Convert tuple to list
# print("after conversion:", type(a)) // Output: after conversion: <class 'list'>

# a.append("vivo")  # Add an element to the list
# print(a)  # Output: ['oneplus', 'samsung', 'apple', 'vivo', 'oppo', 'vivo']

# a=tuple(a)  # Convert list back to tuple
# print("after conversion:", type(a))  # Output: after conversion: <class 'tuple
# print(a)  # Output: ('oneplus', 'samsung', 'apple', 'vivo', 'oppo', 'vivo')

# # Note:- when ever we have to change the tuple elements , we first convert it to list and after it do the changing operation and then again convert it back to tuple.

# functions in tuples:-
# a=("oneplus", "nokia", "redmi")
# 1.print(a.count("redmi"))  # Output: 1 --> counts the number of occurrences of "redmi" in the tuple.
# 2.print(a.index("nokia"))  # Output: 1 --> returns the index of the first occurrence of "nokia" in the tuple.
