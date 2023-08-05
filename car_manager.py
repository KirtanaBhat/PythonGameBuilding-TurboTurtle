from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.car = Turtle("square")
        self.car.hideturtle()
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.color(random.choice(COLORS))
        self.car.penup()
        self.car.goto(300, random.randint(-200, 200))
        self.car.setheading(180)
        self.car.showturtle()
        self.starting_move_distance = 5

    def move_car(self, DIST):
        self.car.forward(DIST)



