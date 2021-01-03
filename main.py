from turtle import Screen
from player import Player
from level import Level
from car_manager import CarManager
import random
import time

screen = Screen()
screen.title("Turtle Crossing Game!")
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

X_COORDINATE = 0
Y_COORDINATE = -280


player = Player()
level = Level()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.is_at_finish_line():
        player.go_to_start()
        level.increase_level()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()