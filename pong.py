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

# Handle the error that is caused by the while loop
# which keeps trying to draw on the canvas after the window is destroyed (closed by user)
# See this StackOverflow post: https://stackoverflow.com/questions/50654793/how-to-detect-x-close-button-in-python-turtle-graphics
canvas = t.getcanvas()
root = canvas.winfo_toplevel()
def on_quit():
    global game_on
    game_on = False

root.protocol("WM_DELETE_WINDOW", on_quit)

game_on = True
while game_on:
    screen.update() # update the screen
    ball_1.move()

    # Detect collision with wall
    # Ball is 20 pixels wide
    # Ball middle point should be at least 20/2 away from the wall
    if abs(ball_1.ycor()) > 290:
        # If hit top/bottom edge of the screen
        # bounce back vertically (y-axis)
        ball_1.bounce_y()
    # if abs(ball_1.xcor()) > 390: 
    #     ball_1.bounce_x()

    # Detect collision with right paddle
    if ball_1.distance(r_paddle) < 50 and ball_1.xcor() > 360:
        ball_1.bounce_x()

    # Challenge: Detect collision with left paddle :)

    
    # Reset position if ball goes out of boundry
    # Detect if right paddle misses the ball
    if ball_1.xcor() > 390:
        ball_1.reset_pos()

    # Challenge: Detect if left paddle misses the ball :)


    if not game_on:
        break