from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE = 10
FINISH_LINE = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.go_to_start()
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False








