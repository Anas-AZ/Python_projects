from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()
        self.goto(-230, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level:{self.level}", False, "center", FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)




