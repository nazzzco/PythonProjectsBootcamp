import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
number_of_frieds = len(friends) - 1
random_number = random.randint(0,number_of_frieds)
print(friends[random_number])
print(random.choice(friends))