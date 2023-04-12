from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        self.color("white")
        self.penup()
        self.dy = 10
        self.dx = 10

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.dy = 10
        self.bounce_x()

    def ball_speed(self):
        self.dy += 5
