from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.goto(-10, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"score:{self.score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
