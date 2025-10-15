from turtle import Turtle

class Ball(Turtle):
    """
    Represents the ball object that bounces between paddles and walls.
    Controls speed and direction of movement.
    """
    def __init__(self):
        """Initialize the ball with starting direction and movement speed."""
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball one step in the current direction."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the vertical direction when hitting the top or bottom wall."""
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverse the horizontal direction when hitting a paddle.
        Increase speed slightly to make the game progressively harder.
        """
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset(self):
        """
        Reset the ball to the center and restore default speed.
        Direction is reversed to give the other player the serve.
        """
        self.home()
        self.move_speed = 0.1
        self.x_move *= -1