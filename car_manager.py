from turtle import Turtle
import random

random_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
location = random.randint(0, 360)
SPEED = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speedd = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(random_colors))
            random_y = random.randint(-200, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.speedd)

    def move_faster(self):
        self.speedd += SPEED



