import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
turt = Player()
screen.setup(width=600, height=600)
screen.tracer(0)

t = 0.1
car = []
dist = 10
x = 6
level = 2

screen.listen()
screen.onkeypress(turt.up, "Up")

game_is_on = True
j = 0

while game_is_on:
    time.sleep(t)
    screen.update()
    if j % x == 0:
        car.append(CarManager())
    for i in car:
        i.move_car(dist)
    j += 2
    toot = turt.check_dead()
    for i in car:
        if i.car.distance(toot) < 20:
            game_is_on = False

    if turt.check_win(level):
        turt = Player()
        level += 1
        dist += 5
        j += 2
        if t > 0:
            t -= 0.01
        else:
            t = 0.01
