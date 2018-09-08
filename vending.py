"""
Baby Snakes, simple Python programs worked out
Algorithm behaves like a vending machine
to make change from a user input number of coins with a limit of $5.00
"""

#DEFINE VARIABLES
PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25

#USER INPUT
userInput = input("Enter bill value:")
billValue = int(userInput)
userInput = input("Enter item price in pennies:")
itemPrice = int(userInput)

#Compute changeDue
changeDue = PENNIES_PER_DOLLAR * billValue - itemPrice
dollarCoins = changeDue // PENNIES_PER_DOLLAR
changeDue = changeDue % PENNIES_PER_DOLLAR
quarters = changeDue // PENNIES_PER_QUARTER
print (dollarCoins, "dollars and", quarters, "quarters")
