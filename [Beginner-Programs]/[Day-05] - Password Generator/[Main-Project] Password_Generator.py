# Category: Beginner
# Main Project: Password Generator
# Date: September 26, 2024

# imports
import random

# Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# greetings
print("Welcome to the LockCode Wizard!")

# user's input
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# [Hard Version]
password_list = []

for char in range (0, nr_letters):
    password_list.append (random.choice (letters))

for char in range (0, nr_symbols):
    password_list.append(random.choice (symbols))
   
for char in range (0, nr_numbers):
   password_list.append (random.choice (numbers))

random.shuffle (password_list)

password = " "
for char in password_list:
    password += char

print (f"Your password is: {password}")

# [Easy Version]
# For Loops
# password = " "

# for char in range (1, nr_letters + 1):
#     password += random.choice (letters)

# for char in range (1, nr_symbols + 1):
#     password += random.choice (symbols)
   
# for char in range (1, nr_numbers + 1):
#    password += random.choice (numbers)

# print (password)
