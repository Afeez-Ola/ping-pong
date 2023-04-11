from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600, startx=350, starty=0)
screen.bgcolor("black")
screen.tracer(0)
left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)

is_game_on = True

while is_game_on:
    screen.tracer(1)

screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")

screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

screen.exitonclick()
