""" pong game main """

import turtle as t
from paddle import Paddle
from ball import Ball

# set up screen
screen = t.Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0) # turn off animation

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

ball_1 = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up") # call-back function
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update() # update the screen
    ball_1.move()

    # Detect collision with wall
    if abs(ball_1.ycor()) > 280: 
        ball_1.bounce_y()
    if abs(ball_1.xcor()) > 380: 
        ball_1.bounce_x()

    # Detect collision with right paddle
    if ball_1.distance(r_paddle) < 50 and ball_1.xcor() > 360:
        ball_1.bounce_x()

    # Detect collision with left paddle, can you do that? :)

    
    # reset position if ball goes out of boundry

    if not game_on:
        break