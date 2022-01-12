from turtle import Turtle, Screen
import random


is_raceon = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_raceon = True

while is_raceon:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_raceon = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
