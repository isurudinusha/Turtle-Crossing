from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    """A class to represent the player turtle."""

    def __init__(self):
        """Initialize the player turtle."""
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.goto(STARTING_POSITION)

    def move(self):
        """Move the player turtle forward."""
        self.turtle.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Reset the player turtle to the starting position."""
        self.turtle.goto(STARTING_POSITION)
