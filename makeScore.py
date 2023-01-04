from turtle import Turtle

class make_a_score(Turtle):
  def __init__(self, x_cor, y_cor, place):
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(x_cor, y_cor)
    self.write(f"Player {place} Score : {self.score}", align="center", font=("Arial", 20, "normal"))
  
  def update_score(self):
    self.clear()
    self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))


