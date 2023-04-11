from turtle import Turtle

paddle = Turtle()

paddle.hideturtle()
paddle.shape("square")
paddle.turtlesize(stretch_wid=5, stretch_len=1, outline=1)
paddle.color("white")
paddle.penup()
paddle.speed("fastest")
paddle.setposition(350, 0)
paddle.showturtle()