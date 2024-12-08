print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path_chosen = input("You're on a crossway. Choose to go on \"left\" or \"right\" ?\n").lower()
if path_chosen == "right":
    print("You fall into a hole. Game Over")
elif path_chosen == "left" or path_chosen == "Left":
    next_step = input("You're in front of a river. Choose to swim or wait\n")
    if next_step == "swim" or next_step == "Swim":
        print("You've been attached by trout. Game Over")
    elif next_step == "wait" or next_step == "Wait":
        door = input("You're in front of 3 doors - red, "
                     "yellow and blue. Which one you're going to choose?\n")
        if door == "yellow" or door == "Yellow":
            print("You win!")
        elif door == "red" or door == "Red":
            print("Burned by fire. Game Over!")
        else:
            print("Eaten by beasts. Game over!")