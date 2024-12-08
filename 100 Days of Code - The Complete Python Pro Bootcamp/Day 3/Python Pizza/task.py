print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

prize = 0
if size == "S":
    prize += 15
    if pepperoni == "Y":
        prize += 2
elif size == "M":
    prize += 20
    if pepperoni == "Y":
        prize += 3
elif size == "L":
    prize += 25
    if pepperoni == "Y":
        prize += 3

if extra_cheese == "Y":
    prize += 1

print(f"Your final bill is: ${prize}.")



