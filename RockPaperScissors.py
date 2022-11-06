# Randomization
# pseudo random generators : Mersenne Twister
# askpython.com 
# Random module can be imported for extra functions using import random
# can import other py files located in same directory
# LIST are data structures
# List : can store multiple data types I.E fruits = [item1, item2]
# List can be updated by: fruits[0] = new data
# Can add to a list by : fruits.append(data) will add to the end of the list. 
# Nested List : allows a list to contain multiple list. 
# def : defines a function i.e def my_function:

import random
import AsciiStrings

GameOptions = ["rock", "paper", "scissors"]


#Main Game Loop
def game_loop():
    playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors "))
    computerChoice = random.randint(0,2)
    #Shows selections
    print("You picked " + GameOptions[playerChoice] + "\n" + AsciiStrings.RockPaperScisccors[playerChoice])
    print("The AI picked " + GameOptions[computerChoice] + "\n" + AsciiStrings.RockPaperScisccors[computerChoice])
    
    #Runs the game #Could of removed the lose elif statements and replaced with an ending "You lose" if it doesn't meet any the win criteria
    if(playerChoice == computerChoice):
        print(AsciiStrings.tied)
    elif(playerChoice == 0 and computerChoice == 1):
        lose_game()
    elif(playerChoice == 0 and computerChoice == 2):
        win_game()
    elif(playerChoice == 1 and computerChoice == 2):
        lose_game()
    elif(playerChoice == 1 and computerChoice == 0):
        win_game()
    elif(playerChoice == 2 and computerChoice == 1):
        win_game()
    elif(playerChoice == 2 and computerChoice == 0):
        lose_game()
    else:
        print("Incorrect Selection")
    playAgain = input("Would you like to play again? Yes or No? ")
    if(playAgain.lower() == "yes" or playAgain.lower() == "y"):
        game_loop()
    else:
        print("Goodbye!")

#Win Function
def win_game():
    print(AsciiStrings.win)
    
#Lose Function
def lose_game():
    print(AsciiStrings.lose)


#Starts us off
playGame = input("Would you like to play rock, paper, scissors? Yes or No? ")
if(playGame.lower() == "yes"):
    game_loop()
else:
    print("Goodbye!")

        
        
