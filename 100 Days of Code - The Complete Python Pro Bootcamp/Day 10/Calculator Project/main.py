from operator import truediv

from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

keep_cicle = True
result = 0.0
to_continue = ""
while keep_cicle:
    if to_continue == "y":
        first_number = result
    else:
        print("\n" * 25)
        print(logo)
        first_number = float(input("What's the first number?: "))

    operator = input("+\n-\n*\n/\nPick an operation: ")
    second_number = float(input("What's the second number?: "))

    calculator_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    # print(calculator_dict["*"](4, 8))

    result = calculator_dict[operator](first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")
    to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
