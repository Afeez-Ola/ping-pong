from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600, startx=350, starty=0)
screen.bgcolor("black")
screen.tracer(0)
left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)

ball = Ball()

is_game_on = True

screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")

screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")
while is_game_on:
    screen.tracer(1)



screen.exitonclick()
