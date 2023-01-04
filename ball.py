from turtle import *
import random

class ball(Turtle):
    def __inti__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        

    def ball_move(self):
        self.forward(20)
        
