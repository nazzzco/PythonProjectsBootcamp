from art import logo, vs
import game_data
import random

def pick_random():
    celebrity = random.choice(game_data.data)
    return celebrity

def compare_game():
    print(logo)

    compare_a = pick_random()

    continue_game = True
    score = 0

    while continue_game:
        compare_b = pick_random()
        if compare_b == compare_a:
            compare_b = pick_random()

        print(f"Compare A: {compare_a["name"]}, a {compare_a["description"]}, from {compare_a["country"]}.")
        print(vs)
        print(f"Against B: {compare_b["name"]}, a {compare_b["description"]}, from {compare_b["country"]}.")
        print(f"{compare_a["follower_count"]} vs {compare_b["follower_count"]}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == 'a' and compare_a["follower_count"] > compare_b["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}.")
        elif user_choice == 'b' and compare_b["follower_count"] > compare_a["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}.")

        compare_a = compare_b

compare_game()
