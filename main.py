from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the player turtle.
player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")

# Create the car manager.
car_manager = CarManager()

# Create the scoreboard.
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car.
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car.
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            time.sleep(1)
            game_is_on = False
            

    # Detect successful crossing.
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.level_up()


    
    

    
