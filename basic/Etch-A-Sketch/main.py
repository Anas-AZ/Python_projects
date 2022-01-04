from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def clockwise():
    tim.rt(10)


def counter_clockwise():
    tim.lt(10)
    # or
    # new_heading = tim.heading() +10
    # tim.setheading(new_heading)


def clear():
    tim.clear()   # deletes only the drawing of this particular turtle
    # whereas the screen.clear() method clears everything on the screen
    tim.penup()
    tim.home()
    tim.pendown()


def undo():
    tim.undo()


screen.listen()
screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.onkey(undo, "u")

screen.exitonclick()
