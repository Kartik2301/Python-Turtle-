from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.level_num = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level {self.level_num}', align="center", font=FONT)

    def increase_score(self):
        self.level_num += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align="center", font=FONT)