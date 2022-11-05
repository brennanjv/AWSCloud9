# Day 2 Notes
# Primitive Data Types
# String : string of characters "abcdefghi"
# Subscripting : can index strings print("Hello"[0]) would output H
# Typecasting
# str(variable) is typecasting as the new variable type.
# Round Numbers
# round() : Can round numbers to a specified number of decimal places I.E round(2.3333, 2) will round to 2.33
# print(f) : Allows to place variables in strings without having to typecast using {}

#Gets all the neccesary input from user, Bill, Tip Percentage, Number of people to split bill
print("Welcome to the tip calculator")
billAmount = float(input("What was the total bill? "))
tipAmount = float(input("How much would you like to tip? "))
amountOfPeople = int(input("How many people are splitting the bill? "))

#Calculates the total per person
tipPercentage = tipAmount / 100
tipAmount = tipPercentage * (billAmount)
finalAmount = round(billAmount + tipAmount,2)
costPerPerson = round(finalAmount / amountOfPeople,2)

#Prints out the results. Show both typecasting and the print(f) function
print("The total bill with tip is $" + str(finalAmount)) 
print(f"Each person should pay ${costPerPerson}")