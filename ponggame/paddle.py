from turtle import Turtle

class Paddle(Turtle):
    """
    Represents a paddle in the Pong game.
    Controlled by the player to hit the ball back and forth.
    """
    def __init__(self, position):
        """Initialize the paddle at a given position (left or right side)."""
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        """Move the paddle up by 20 pixels (within the upper boundary)."""
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        """Move the paddle down by 20 pixels (within the lower boundary)."""
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
