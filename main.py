# TODO Create the screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Configuration
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping-Pong")
screen.tracer(0)


# TODO Create and move a paddle
# Creating Right and Left Pallets
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# TODO Create the ball and make it move
# Creating the ball
ball = Ball()

# TODO Keep score
# Creating Scoreboard Object
scoreboard = Scoreboard()

# Paddles Control
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game Execution
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO Detect collision with wall and bounce
    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce
        ball.bounce_y()

    # TODO Detect collision with paddle
    # Detect Collision with the Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        # Bounce
        ball.bounce_x()

    # TODO Detect when Right paddle misses
    # Detect Right Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # TODO Detect when Left paddle misses
    # Detect Left Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
