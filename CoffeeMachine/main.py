from itertools import dropwhile

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def check_resources(choice):
    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

'''
    is_sufficient = True
    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("Sorry, there's not enough water.")
        is_sufficient = False
    if resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry, there's not enough coffee.")
        is_sufficient = False
    if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print("Sorry, there's not enough milk.")
        is_sufficient = False
    return is_sufficient
'''

def process_coins(drink):
    is_enough = True
    print("Please insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickels = int(input("how many nickels? "))
    pennies = int(input("how many pennies? "))
    total_sum = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if total_sum >= MENU[drink]["cost"]:
        change = round(total_sum - MENU[drink]["cost"], 2)
        resources["money"] += MENU[drink]["cost"]
        print(f"Here's ${change} dollars in change")
    else:
        print("Sorry, that's not enough money. Money refunded.")
        is_enough = False
    return is_enough

def make_coffee(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    print(f"Here's your {choice} ☕. Enjoy!")

prompt = ""
while prompt != "off":
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "report":
        report()
    elif check_resources(prompt):
        if process_coins(prompt):
            make_coffee(prompt)