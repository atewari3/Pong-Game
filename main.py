import turtle
from turtle import Turtle, Screen
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle_line import MiddleLine

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

middle = MiddleLine()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

ball = Ball()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.restart()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.restart()


screen.exitonclick()
