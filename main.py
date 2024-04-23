from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(right_paddle) < 50) or (ball.xcor() < -320 and ball.distance(left_paddle) < 50):
        ball.bounce_x()

    if (ball.xcor() > 380):
        ball.reset_position()
        score_board.left_point()
    
    if (ball.xcor() < -380):
        ball.reset_position()
        score_board.right_point()


screen.exitonclick()