from turtle import Turtle

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("black")
        self.goto(0, 0)
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.move_speed *= 0.9

