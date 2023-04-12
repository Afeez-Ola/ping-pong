from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600, startx=350, starty=0)
screen.bgcolor("black")
screen.tracer(0)
left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)

ball = Ball()

scoreboard = Scoreboard()

is_game_on = True

screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")

screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")
while is_game_on:
    time.sleep(.04)
    screen.tracer(1)
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        # time.sleep(.04)
        ball.bounce_y()
    # Detect paddle collision
    if ball.distance(left_paddle) < 50 and ball.xcor() > 320 or ball.distance(right_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 350:
        time.sleep(0.6)
        ball.reset_ball()
    elif ball.xcor() < -350:
        time.sleep(0.6)
        ball.reset_ball()

screen.exitonclick()
