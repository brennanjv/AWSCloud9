#Password Generator
import string
import random
print("Welcome to Brennan's Password Generator")

#Asking user for complexity of password
numberOfLetters = int(input("How many letters would you like? \n"))
numberOfSymbols = int(input("How many symbols would you like? \n"))
numberOfNumbers = int(input("How many numbers would you like? \n"))

#Variables for our letters,numbers,symbols
Alphabet = list(string.ascii_letters)
Numbers = list(string.digits)
Symbols = list(string.punctuation)

password = ""
#Generates all the neccesarry requirements and appends to our password
for x in range(0,numberOfLetters):
    password += random.choice(Alphabet)
for x in range(0, numberOfSymbols):
    password += random.choice(Symbols)
for x in range(0, numberOfNumbers):
    password += random.choice(Numbers)
    
passwordInList = list(password)
random.shuffle(passwordInList)
password = "".join(passwordInList)
    
print(password)