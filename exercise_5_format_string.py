#Exercise 5: Using format strings to print a message

#Define the variables
first_name = "John"
last_name = "Doe"
balance = 53.44

#Use a format string to display the message
message = f"Hello {first_name} {last_name}. Your current balance is ${balance:.2f}"
print(message)



#Explanation
#f-string(f"...")

#allows you to insert variables directly into strings.

#{balance:.2f} ensures the balance always shows 2 decimal places


#Out will be:

#Hello John Doe. Your current balance is $5.44


message = "Hello {} {}. Your current balance is ${:.2f}".format(first_name, last_name, balance)
