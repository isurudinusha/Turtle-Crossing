from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """A class to represent the scoreboard."""

    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-380, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increase the level by 1."""
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    
    def game_over(self):
        """Display the game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)