import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()

screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")

score = Scoreboard()

car=CarManager()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:
        car.create_car()
    car.move_cars()
    for carr in car.all_cars:
        if player.distance(carr) < 25:  
            score.game_over()
            game_is_on = False

    if player.reset_position():
        player.goto_start()
        car.level_up()
        score.score_update()
        


screen.exitonclick()
