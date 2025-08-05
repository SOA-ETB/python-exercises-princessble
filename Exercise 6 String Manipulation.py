#Exercise 6: String Manipulation
text = "  Hello, World! Welcome to python coding.  "

#For the sample text, do the following manipulations:
#1. count occurrences: Count how many times the letter o appear in the string

count_o = text.count("o")
print("Occurrences of 'o':", count_o)


#2. Strip leading and trailing spaces:
stripped_text = text.strip()
print("Stripped text:", stripped_text)


#3. Extract the substring "World" using range slicing:
# First, strip the text to remove whitespace so we can slice properly
stripped_text = text.strip()
substring_world = stripped_text[7:12]
print("Substring 'World':", substring_world)


#4. Reverse the entire string:
reversed_text = text[::-1]
print("Reversed text:", reversed_text)


#5.  Check if the string starts with "Hello":
starts_with_hello = text.strip().startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

#6. Check if the string ends with "programming":
ends_with_programming = text.strip().endswith("programming")
print("Ends with 'programming':", ends_with_programming)


#7. Split the string into a list of words:
word_list = text.strip().split()
print("List of words:", word_list)


#8. Print the string with a new line between "World!" and "Welcome":
# Replace 'World! Welcome' with 'World!\nWelcome'
modified_text = text.strip().replace("World! Welcome", "World!\nWelcome")
print("Modified text with new line:\n", modified_text)
