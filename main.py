from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()

screen.setup(width=800, height=600, startx=350, starty=0)
screen.bgcolor("black")
screen.tracer(0)
paddle1 = Paddle()
paddle2 = Paddle().new_paddle()


def up():
    paddle1.sety(paddle1.ycor() + 40)


def down():
    paddle1.sety(paddle1.ycor() - 40)

is_game_on = True

while is_game_on:
    screen.tracer(1)

screen.onkey(up, "Up")
screen.onkey(down, "Down")

screen.listen()

screen.exitonclick()
