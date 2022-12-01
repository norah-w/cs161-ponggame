# Ball class

from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("lightblue")
        self.shape("circle")
        self.penup()
        self.y_step = 0.5
        self.x_step = 0.5
    
    def move(self):
        x_cor = self.xcor() + self.x_step 
        y_cor = self.ycor() + self.y_step 
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_step  *= -1
    
    def bounce_x(self):
        self.x_step  *= -1



