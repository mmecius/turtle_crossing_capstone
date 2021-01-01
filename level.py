from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pen()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Courier", 25, "normal"))

    def increase_level(self):
        self.score += 1
        self.update()

