from art import logo
print(logo)
# TODO-1: Ask the user for input
bidders_dictionary = {}

stop_game = False
while not stop_game:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    # TODO-2: Save data into dictionary {name: price}
    bidders_dictionary[name] = bid
    #bidders_dictionary = bidders_dictionary
    print(bidders_dictionary)
    # TODO-3: Whether if new bids need to be added
    ask_to_stop = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ask_to_stop == "no":
        stop_game = True
    else:
        print("\n" * 100)
# TODO-4: Compare bids in dictionary
biggest = 0
biggest_name = ""
for key in bidders_dictionary:
    if int(bidders_dictionary[key]) > biggest:
        biggest = int(bidders_dictionary[key])
        biggest_name = key
print(f"The winner is {biggest_name} with a bid of ${biggest}")

