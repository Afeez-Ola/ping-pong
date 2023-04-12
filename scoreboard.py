from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_point = 0
        self.r_point = 0
        self.goto(-100, 180)
        self.write(self.l_point, align="center", font=("Courier", 80, "normal"))

    def l_score(self):
        self.l_point += 1

    def r_score(self):
        self.r_point += 1
