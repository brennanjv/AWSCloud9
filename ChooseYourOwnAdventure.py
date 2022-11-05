#Notes for Day 3
#if statements
# if condition:
#   do this
# else:
#   do this instead
#Logical Operators : and / or / not
print("Welcome to Brennan's Choose Your Own Adventure Game")
play = input("Are you ready to start? Y/N\n")
if(play.lower() == "y"):
    print("Your goal is to survive and find the treasure!")
    selection_1 = input("You are at a crossroads, do you go left or right?\n")
    if selection_1.lower() == "left":
        selection_2 = input("You end up at a cemetery, what do you do \n A. go around \n B. go through the gates.\n")
        if selection_2.lower() == "a":
            selection_3 = input("Good choice! You arrive at 3 strange chest. Which one do you open? 1,2 or 3? ")
            if selection_3 == "1":
                print("The chest is a mimic! It eats you!\n GAME OVER!")
            elif selection_3 == "2":
                print("You open the chest and find a bunch of jewels and gold!\n CONGRATULATIONS YOU'VE WON")
            else:
                print("You open the chest and find nothing. At-least your alive?\n GAME OVER!")
        else:
            print("A gang of skeletons attack you and bury you into the ground\n GAME OVER!")

    else:
        if selection_1.lower() == "right":
            print("The ground caves below your feet and you fall to your death!")
            print("GAME OVER!")
else:
    print("Goodbye!")