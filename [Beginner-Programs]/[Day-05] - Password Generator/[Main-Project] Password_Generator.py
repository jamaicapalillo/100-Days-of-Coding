# 100 DAYS OF CODE
# CATEGORY: BEGINNER
# Date: September 26, 2024

# Main Program:  PASSWORD GENERATOR
# Programmed by: Palillo, Jamaica C.

# -------------------------------------------

# Instruction: (Easy Version)
# Generate the password in sequence. Letters, then symbols , then numbers.

# -------------------------------------------

# Imports
import random

# Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Greetings
print("Welcome to the LockCode Wizard!")

# User's input
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

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