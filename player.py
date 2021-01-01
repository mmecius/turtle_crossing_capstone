from turtle import Turtle
X_COR = 0
Y_COR = -280
MOVE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(X_COR, Y_COR)
        self.left(90)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)





