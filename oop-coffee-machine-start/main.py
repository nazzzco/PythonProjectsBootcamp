from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

prompt = ""
while prompt != "off":
    options = menu.get_items()
    prompt = input(f"What would you like ({options})?: ").lower()
    if prompt == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

