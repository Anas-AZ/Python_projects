from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # it will be stretched by 0.5 ie, 20x0.5 =10 (10x10 circle)
        self.color("blue")
        self.speed("fastest")  # increase speed, so that we can't see it appearing
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)  # screen is 300x300 so to be inbounds we use 270
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
