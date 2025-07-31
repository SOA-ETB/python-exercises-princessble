#Exercise 4: adding values to lists and performing calculations
#1. Create a list named 'numbers' and add 1, 2, 3 to it
numbers = [1, 2, 3]

#perform 3 different calculations using operators
sum_numbers = numbers[0] + numbers[1] + numbers[2] #1 + 2 + 3
product_numbers = numbers[0] * numbers[2]
difference = numbers[2] - numbers[0]

print("Sum of numbers:", sum_numbers)
print("Product of first and last number:", product_numbers)
print("Difference between last and first number:", difference)

#2 Create a list named 'names' and  add some initial names
names = ["Sam", "Blessing", "Victoria"]

#Use append() to add another name
names.append("Conor")

print("Names list after appending:", names)