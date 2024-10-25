# DAY 3
# Date: September 22, 2024

# Program Exercise: Ticket Booth Selling

# ========================

# Greetings
print ("WECLOME TO THE WHILRWIND WOMBAT!!!")

# Add the Rides Rule
print ("\nBelow are the rules and regulations for our ride. Kindly read it first before buying a ticket.")
print ("\n1. The person must be 120 cm.")
print ("\n2. The person must be 13 and above.")
print ("\n3. The person below 13 must have a guardian with them.")
print ("\n4. Thank you!\n")
        
# Check if person can join the ride
height = float (input ("What is your height? "))

# Check the person's height
if height >= 120:
    print ("\nYou are qualified to ride our ride.\n")
    # Check the person's age
    age = int (input ("What is your age: "))
    if age < 12:
        ticket = 7
    elif age >= 18 and age <45:
        ticket = 12
    elif 45 <= age <=55:
        ticket = 0
        print ("The ticket is free!!")
    else:
        ticket = 5

    # Do you want to add photo or not?
    photo = False
    add_photo = input ("\nDo you want to add photos? Yes or No? ")
    if add_photo == "Yes":
        add_price = 3
        ticket = add_price + ticket
    else:
        print ("Alright.\n")

else:
    print ("We're sorry. Guess you still need to grow a little bit to be able to join the ride.")

# Display the ticket price
print (f"\nYour ticket price would be ${ticket}. Thank you and have a nice ride!")