from turtle import Screen
from player import Player

screen = Screen()
screen.title("Turtle Crossing Game!")
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True

while game_is_on:
    screen.update()
    pass

screen.exitonclick()