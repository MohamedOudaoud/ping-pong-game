from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
sleeper = 0.1

while game_on:
    screen.update()

    # start moving the ball
    time.sleep(sleeper)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    # discover the collision with the roof and the bottom
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1

    # discover the collision with the paddles
    if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= -330 and ball.distance(l_paddle) <= 50):
        ball.x_move *= -1
        sleeper *= 0.9

    # if it exit from the right side
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.x_move *= -1
        score.l_point()
        sleeper = 0.1

    # if it exit from the left side
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.x_move *= -1
        score.r_point()
        sleeper = 0.1




screen.exitonclick()