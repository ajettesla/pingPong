from turtle import Turtle


class paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=8, outline=None)
        self.penup()
        self.setheading(90)
        self.goto(-485, 0)

    def move(self):
        self.forward(20)
