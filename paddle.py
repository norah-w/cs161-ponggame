""" Paddle class """

from turtle import Turtle

class Paddle(Turtle):
    """ Subclass of Turtle class """

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1) # width (20 * 5 pixels), len (20 * 1 pixels)
        # wed
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 10)
        self.check_boundry()

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 10)
        self.check_boundry()
    
    def check_boundry(self):
        """ Stop paddle from going out of the boundry
        of the top or bottom of the screen.
        """
        # Paddle height is 100 pixels
        # Paddle middle point should be at least 100/2 pixels
        # away from the top/bottom edge of the screen
        if (self.ycor() < -250):
            self.goto(self.xcor(), -250)
        if (self.ycor() > 250):
            self.goto(self.xcor(), 250)