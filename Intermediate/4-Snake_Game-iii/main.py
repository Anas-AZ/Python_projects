from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
DELAY = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # Turn off the animation
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(DELAY)  # introduces a delay
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # checks the distance of snake from food (15 is added as a buffer)
        food.refresh()
        snake.extend()
        score.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
