import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.drive()

    # Detect player collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    # Detect player crossing the finish line
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.increase_speed()
        score.increase_level()


screen.exitonclick()
