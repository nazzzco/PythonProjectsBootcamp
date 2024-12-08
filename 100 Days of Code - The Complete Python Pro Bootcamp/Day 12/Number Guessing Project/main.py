import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

def play_game():
    number = random.randint(1,100)
    print(f"Psst, this is the number: {number}")
    attempts = 0
    final = "Guess again."
    if mode == "easy":
        attempts = 10
    elif mode == "hard":
        attempts = 5

    for i in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {guess}.")
            break
        elif guess > number:
            if attempts == 1:
                final = "You've run out of guesses, you lose."
            print(f"Too high.\n{final}")
        elif guess < number:
            if attempts == 1:
                final = "You've run out of guesses, you lose."
            print(f"Too low.\n{final}")

        attempts -= 1

play_game()