import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_rps = [rock, paper, scissors]
comp_choice = random.choice(list_rps)
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice == 0:
    print(rock)
    print(f"Computer chose:\n{comp_choice}")
    if comp_choice == rock:
        print("It's a draw!")
    elif comp_choice == paper:
        print("You lose!")
    elif comp_choice == scissors:
        print("You win!")
elif your_choice == 1:
    print(paper)
    print(f"Computer chose:\n{comp_choice}")
    if comp_choice == paper:
        print("It's a draw!")
    elif comp_choice == scissors:
        print("You lose!")
    elif comp_choice == rock:
        print("You win!")
elif your_choice == 2:
    print(scissors)
    print(f"Computer chose:\n{comp_choice}")
    if comp_choice == scissors:
        print("It's a draw!")
    elif comp_choice == rock:
        print("You lose!")
    elif comp_choice == paper:
        print("You win!")