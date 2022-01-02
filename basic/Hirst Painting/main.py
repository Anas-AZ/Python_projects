color_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191)]
# TODO: 10x10 rows of spots
# TODO 2:each dot's size = 20
# TODO 3:each dot spaced apart by 50 paces
import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
tim.ht()
tim.penup()
tim.speed(0)
tim.setheading(225)
tim.fd(350)
tim.setheading(0)
for i in range(10):
    for j in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
