#Create a function that checks if an input number is even or odd.
#it should be able to take an input number from the user, and display the result,
#it should continue to ask the user for input values until the uer chooses
#to end the interaction( i.e with a loop and an option to quit the exercise/game)

def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

while True:
    user_input = input("Enter a number to check (or type 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Thank you for using the Even/Odd checker. Goodbye!")
        break

    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        check_even_or_odd(number)
    else:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
