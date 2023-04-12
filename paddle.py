from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()

        self.speed("fastest")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=1)
        self.color("white")
        self.penup()
        self.setposition(xcor, ycor)

    def go_up(self):
        new_y = self.ycor() + 60
        self.setposition(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 60
        self.setposition(self.xcor(), new_y)
