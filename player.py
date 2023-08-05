from turtle import Turtle
import time

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270

toot = Turtle("turtle")
display = Turtle()
display.hideturtle()


class Player:
    def __init__(self):
        toot.penup()
        toot.goto(STARTING_POSITION)
        toot.setheading(90)

    def up(self):
        toot.forward(MOVE_DISTANCE)

    def check_win(self, level):
        if toot.ycor() == FINISH_LINE_Y:
            display.write(f"LEVEL {level}")
            time.sleep(1.5)
            display.clear()
            toot.goto(STARTING_POSITION)
            return True

    def check_dead(self):
        return toot
