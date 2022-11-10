# Pokemon Hangman Project
# To Do List
# Create a word-list and have the code select a random word on each play
# Ask the player to guess a letter and check if that letter is one in our word
import random
import AsciiStrings

word_list = ["charizard", "blastoise", "venasaur", "pikachu", "eevee", "tyranitar", "lopunny", "flygon", "regirock", "turtwig"]

chosen_word = random.choice(word_list)
#for testing
#chosen_word = word_list[0]

#Keeps track of incorrect guesses
incorrectGuesses = 0
#Checks if we have won!
hasWon = False

#Creates our display
display = []
for letter in chosen_word:
    display.append("_")
    
#Keeps Track of guessed words
guessed_letters = [""]

print(AsciiStrings.hangman[incorrectGuesses])

while incorrectGuesses < 6 and hasWon == False:
    #Shows our display
    print(display)
    
    # Ask User for a guess
    guess = str(input("Please guess a letter. \n").lower())
    
    #penalizes for guessing same letter twice
    badGuess = False
    for x in guessed_letters:
        if guess == x:
            badGuess = True
            print("This has already been guessed")
    guessed_letters.append(guess)
            
    # Checks if guess is correct and edits our display with addtions
    currentPos = -1
    choseCorrect = False
    for letter in chosen_word:
        currentPos += 1
        if(guess == letter):
            choseCorrect = True
            display[currentPos] = guess
    
    #Checks for our win
    win_check = "".join(display)
    if win_check == chosen_word:
        hasWon = True
    
    #Adds the penalty for being a repeat guess
    if badGuess:
        choseCorrect = False
        
    
    #Adds 1 to our incorrect guesses
    if choseCorrect == False:
        incorrectGuesses += 1
        print("You have chosen incorrectly!")
    else:
        print(f"You correctly guessed {guess}")
    print(AsciiStrings.hangman[incorrectGuesses])    

#Win/Lose Conditions
if incorrectGuesses == 6:
    print(f"{AsciiStrings.lose}\nThe word was {chosen_word}")
    
if hasWon == True:
    print(f"{AsciiStrings.win}\nThe word was {chosen_word}")