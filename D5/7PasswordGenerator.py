#Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# We have a password that started out as an empty string
# We use a for loop to add the letters, symbols and numbers to the password
# We use the random.choice() function to randomly select a letter, symbol or number from the list
# We add the random letter, symbol or number to the password

password = ""
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

# We print the password with order, first the letters, then the symbols and finally the numbers
# This is the easy way
# print(password)

# We use the shuffle function from the random module
# We convert the string into a list
# We shuffle the list
# We convert the list back into a string
# We print the password

shuffle_password = list(password)
random.shuffle(shuffle_password)
password = "".join(shuffle_password) # The join() method will concatenate the list's elements into a new string and return it as output
# We print the password with random order
print(password)