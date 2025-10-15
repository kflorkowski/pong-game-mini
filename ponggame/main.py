from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


import time
LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Object creation
l_paddle = Paddle(LEFT_POSITION)
r_paddle = Paddle(RIGHT_POSITION)
ball = Ball()
scoreboard = Scoreboard()

# Keyboard event listeners
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(l_paddle) < 60 and ball.xcor() == -330 or ball.distance(r_paddle) < 60 and ball.xcor() == 330:
        ball.bounce_x()

    #Detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_score()

    #Detect l_paddle misses
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.right_score()

screen.exitonclick()