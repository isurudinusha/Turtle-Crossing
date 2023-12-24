from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """A class to represent the player turtle."""

    def __init__(self):
        """Initialize the player turtle."""
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        """Move the player turtle forward."""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Reset the player turtle to the starting position."""
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        """Return True if the player turtle is at the finish line."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
