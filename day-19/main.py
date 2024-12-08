import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for t in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[t])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

# def move_forwards():
#     eti.forward(10)
#
# def move_back():
#     eti.backward(10)
#
# def turn_left():
#     new_heading = eti.heading() + 10
#     eti.setheading(new_heading)
#
# def turn_right():
#     new_heading = eti.heading() - 10
#     eti.setheading(new_heading)
#
# def clear():
#     eti.clear()
#     eti.penup()
#     eti.home()
#     eti.pendown()
#     #screen.clearscreen()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

