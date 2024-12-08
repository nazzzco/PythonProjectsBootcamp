def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(1, 3, 4, 5, 6, 7))

def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)
