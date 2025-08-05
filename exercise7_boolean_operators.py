#Exercise 7: Boolean Operators
#Change each variable in the example to ensure all expressions evaluate to True

number = 10
second_number = 10
first_array = []
second_array = [1, 2, 3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")



#What’s Wrong and How to Fix Each:
#1.  number > 15 → 10 is not greater than 15 →
#2.  if first_array: → [] is falsy →
#3.  len(second_array) == 2 → [1, 2, 3] length is 3 →
#4.  len(first_array) + len(second_array) == 5 → 0 + 3 = 3 →
#5.  if first_array and first_array[0] == 1: → first_array is empty →
#6.  if not second_number: → 10 is truthy → not 10 is False →


#Corrected Code (All expressions evaluate to True):

number = 20                     # greater than 15 
second_number = 0              # falsy value 

first_array = [1, 2]           # non-empty list 
second_array = [1, 2, 3]       # has 3 elements 

if number > 15:
    print("1")                 # True

if first_array:
    print("2")                 # True

if len(second_array) == 3:
    print("3")                 #  True

if len(first_array) + len(second_array) == 5:
    print("4")                 # True (2 + 3 = 5)

if first_array and first_array[0] == 1:
    print("5")                 # True (first element is 1)

if not second_number:
    print("6")                 # True (0 is falsy, not 0 is True)
