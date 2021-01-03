from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)





