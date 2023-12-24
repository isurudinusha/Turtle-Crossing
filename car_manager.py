from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """A class to represent the car manager."""

    def __init__(self):
        """Initialize the car manager."""
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a new car."""
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(400, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        """
        The function moves the cars backwards.
        """
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase the car speed."""
        self.car_speed += MOVE_INCREMENT
