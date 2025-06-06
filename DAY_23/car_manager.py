from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT
    
    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        car.goto(300, random_y)  # Start from right side
        car.setheading(180)
        car.goto(300, random_y)
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def clear_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()

    def level_up(self):
        self.car_speed += self.increment





    
        
    
