from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.setup(width=800, height=600, startx=350, starty=0)
screen.bgcolor("black")
turtle.hideturtle()
turtle.shape("square")
turtle.turtlesize(stretch_wid=5, stretch_len=1, outline=1)
turtle.color("white")
turtle.penup()
turtle.speed("fastest")
turtle.setposition(350, 0)
turtle.showturtle()


def up():
    turtle.sety(turtle.ycor() + 40)


def down():
    turtle.sety(turtle.ycor() - 40)


screen.onkey(up, "Up")
screen.onkey(down, "Down")

screen.listen()

screen.exitonclick()
