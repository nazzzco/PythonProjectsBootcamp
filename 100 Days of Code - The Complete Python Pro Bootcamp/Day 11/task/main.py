import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(list_of_cards, times):
    for i in range(times):
        list_of_cards.append(random.choice(cards))
    return list_of_cards

def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21:
        return 0
    elif sum(list_of_cards) > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)
    else:
        return sum(list_of_cards)

def compare_final_scores(score1, score2):
    if score1 == score2:
        return print(f"{score1} = {score2} - it's a draw!")
    elif score1 > score2:
        return print(f"{score1} > {score2} - you win!")
    else:
        return print(f"{score1} < {score2} - you lose!")

should_restart = True

while should_restart:
    your_cards = []
    computer_cards = []
    your_cards = deal_card(your_cards, 2)
    computer_cards = deal_card(computer_cards, 2)
    print(your_cards)
    print(computer_cards)

    your_score = calculate_score(your_cards)
    comp_score = calculate_score(computer_cards)

    print(your_score)
    print(comp_score)

    another_card = ""
    should_repeat = True
    while should_repeat:
        if your_score == 0:
            print("you win")
            should_repeat = False
        elif comp_score == 0:
            print("computer wins!")
            should_repeat = False
        elif your_score > 21:
            print("you lose")
            should_repeat = False
        elif your_score < 21 and comp_score > 21:
            print("you win")
            should_repeat = False
        elif your_score < 21 and another_card != 'n':
            another_card = input("Will you draw another card? ")
            if another_card == 'y':
                should_repeat = True
                deal_card(your_cards, 1)
                your_score = calculate_score(your_cards)
                print(f"Your score: {your_score}")
        elif comp_score < 17:
            should_repeat = True
            deal_card(computer_cards, 1)
            comp_score = calculate_score(computer_cards)
            print(f"Computer score: {comp_score}")
        else:
            should_repeat = False
            compare_final_scores(your_score, comp_score)

    restart = input("Do you want a new game? :")
    if restart == 'y':
        should_restart = True
    if restart == 'n':
        should_restart = False
