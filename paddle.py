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


    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)