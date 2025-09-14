# List are represented inside-[]
# Tuples are represented inside-()
# Dictionaries are represented inside-{} //braces or curly brackets


# Employee_Data = {"name": "john","age": 14,"gender":"male"}
# print (Employee_Data) --> output- {'name': 'john', 'age': 14, 'gender': 'male'}
# print(Employee_Data["gender"]) ---> male

# Iteration in disctionaries:
# student={"name":"John","class":"6th","roll_no":"23",}
# print(student["roll_no"])

# printing all the key names one by one :
# for x in student:
#     print(x)

# printing all the value names one by one :
# for x in student:
#     print(student[x])

#  using value function
# for x in student.values():
#     print(x)

#  using items function ---> printing both keys and values simultaneously
# for x,y in student.items():
#     print(x," ",y)


# functions in dictionaries: (PART-1)
# student={"name":"John","class":"6th","roll_no":"23",}

# get:
# x= student.get("roll_no")
# print(x)  # Output: 23 --> retrieves the value associated with the key "

# items:
# a= student.items()
# print(a)  # Output: dict_items([('name', 'John'), ('class', '6th'), ('roll_no', '23')])        

# keys:
# a= student.keys()
# print(a)  # Output: dict_keys(['name', 'class', 'roll_no']) --> retrieves all the keys in the dictionary.

# values:
# a= student.values()
# print(a)  # Output: dict_values(['John', '6th', '23']) --> retrieves all the values in the dictionary.

# copy:
# a= student.copy()
# print(a)  # Output: {'name': 'John', 'class': '6th', 'roll_no': '23'} --> creates a shallow copy of the dictionary.   

# functions in dictionaries: (PART-2)

# student={"name":"John","class":"6th","roll_no":"23",}

# setdefault:
# a= student.setdefault("age", 14)
# x= student.setdefault("age", 14)
# print(x)  # Output: 14 --> retrieves the value associated with the key "age" or sets it to 14 if it doesn't exist.  
# print(student)  # Output: {'name': 'John', 'class': '6th', 'roll_no': '23', 'age': 14} --> updates the dictionary with the new key-value pair.        

# update:
# student.update({"age": 14})
# print(student)  # Output: {'name': 'John', 'class': '6th', 'roll_no': '23', 'age': 14} --> updates the dictionary with the new key-value pair.    

# pop:
# a= student.pop("roll_no")
# print(a)  # Output: 23 --> removes the key "roll_no" and returns its value.
# print(student)  # Output: {'name': 'John', 'class': '6th', 'age': 14} --> updates the dictionary after removing the key-value pair.

# popitem:
# a= student.popitem()  
# print(a)  # Output: ('age', 14) --> removes the last inserted key-value pair and returns it.  
# print(student)  # Output: {'name': 'John', 'class': '6th'} --> updates the dictionary after removing the last inserted key-value pair.

# clear:
# student.clear()
# print(student)  # Output: {} --> removes all items from the dictionary, resulting in  an empty dictionary.    

# Nested Dictionaries:-
# Employee= {1: {"name": "John", "age": 24},
#            2: {"name": "Lisa", "gender": "female"}}
# here major keys are 1 and whole bracket inside it are major vslues , and inside bracket the name are minor keys and john are the minor values.


# Employee= {1: {"name": "John", "age": 23 , "Gender":"male"},
#             2: {"name": "Lisa","age": 24, "gender": "female"},
#              3:{"name": "peter","age": 22, "gender": "male" }}

           
# print(Employee)
# print(Employee[2])
# print(Employee[2]["age"])