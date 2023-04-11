from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.speed("fastest")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=1)
        self.color("white")
        self.penup()
        self.setposition(350, 0)

    def new_paddle(self):
        position = (-350, 0)
        self.setposition(position)
