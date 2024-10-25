# DAY 3
# Date: September 22, 2024

# Program: Pizza Order

# ========================

# Greetings
print ("Welcome to Slice of Life Deliveriees!!")

# Sizes
print ("\nPizza Sizes Guide")
print ("\nSmall Pizza: $12")
print ("\nMedium Pizza: $15")
print ("\nLarge Pizza: $18")

# Ask what size of the pizza
size_of_pizza = input ("\nWhat size of pizza do you want? S, M or L: ")

if size_of_pizza == "S":
    price = 12
elif size_of_pizza == "M":
    price = 15
elif size_of_pizza == "L":
    price = 18
else:
    print ("\nUnavaiable.")

# Ask if they want pepperoni
pepperoni = input ("\nDo you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    additional = 2
    price = price + additional
else:
    print ("Noted.")

# Ask if they want some extra_cheese
extra_cheese = input ("\nDo you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    additional = 1.50
    price = price + additional
else:
    print ("Noted.")

# Display Total Price:
print (f"\nYour Total Price is ${price}. Thank You!")