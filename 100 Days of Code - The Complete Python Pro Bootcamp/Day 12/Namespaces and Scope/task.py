enemies = 0


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    return enemies


increase_enemies()
print(f"enemies outside function: {enemies}")
