# DAY 2 FINAL PROGRAM: TIP CALCULATOR

# Greetings! 
print ("Welcome to the Tip Calculator!!")

# Total Bill
bill = float(input("What was the total bill? "))

# Tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

if tip == 10:
    tip_total = (bill * 0.10)
    total = (bill + tip_total)
elif tip == 12:
    tip_total = (bill * 0.12)
    total = (bill + tip_total)
elif tip == 15:
    tip_total = (bill * 0.15)
    total = (bill + tip_total)
else:
    tip_total = (bill * (tip / 100))

total = (bill + tip_total)

# How many people?
split_bill = int(input("How many people to split the bill? "))
split_bill_total = (total / split_bill)

# How each person should pay?
print (f"Each person should pay: {split_bill_total:.2f}")
