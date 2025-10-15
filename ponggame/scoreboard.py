from turtle import Turtle


FONT = ('Calibri', 18, 'normal')

class Scoreboard(Turtle):
    """
    Displays and updates the score during the game.
    Keeps track of both players' points.
    """
    def __init__(self):
        """Initialize the scoreboard with starting scores."""
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        """Refresh the scoreboard display."""
        self.clear()
        self.write(f"{self.l_score}:{self.r_score}", font=FONT)

    def left_score(self):
        """Increase left player's score by 1."""
        self.l_score += 1
        self.score_update()

    def right_score(self):
        """Increase right player's score by 1."""
        self.r_score += 1
        self.score_update()