from turtle import *
import slides_placement
import makeScore
import time
import random

gameisOn = True
directions = [45, 135, -45, -135]

screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 750)
tracer(0)
paddle_1 = slides_placement.paddle()
paddle_1.goto(-485, 0)
paddle_2 = slides_placement.paddle()
paddle_2.goto(485, 0)
score_1 = makeScore.make_a_score(-200, 300, 1)
score_2 = makeScore.make_a_score(200, 300, 2)
ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.setheading(45)
ball.penup()


def player_1_up():
    paddle_1.setheading(90)
    paddle_1.move()


def player_2_up():
    paddle_2.setheading(90)
    paddle_2.move()


def player_1_down():
    paddle_1.setheading(270)
    paddle_1.move()


def player_2_down():
    paddle_2.setheading(270)
    paddle_2.move()


def reflect():
    if ball.heading() == 45:
        ball.setheading(315)
    elif ball.heading() == 315:
        ball.setheading(45)
    elif ball.heading() == 225:
        ball.setheading(135)
    elif ball.heading() == 135:
        ball.setheading(225)


def paddle_ball_reflect():
    if ball.heading() == 45:
        ball.setheading(135)
    elif ball.heading() == 135:
        ball.setheading(45)
    elif ball.heading() == 225:
        ball.setheading(315)
    elif ball.heading() == 315:
        ball.setheading(225)


def paddle_reflect():
    if paddle_1.distance(ball.position()) < 60 and ball.xcor() < -480:
        paddle_ball_reflect()

    if paddle_2.distance(ball.position()) < 60 and ball.xcor() > 480:
        paddle_ball_reflect()


while gameisOn:
    screen.onkeypress(player_1_up, "w")
    screen.onkeypress(player_1_down, "s")
    screen.onkeypress(player_2_up, "8")
    screen.onkeypress(player_2_down, "2")
    screen.listen()
    ball.forward(20)
    paddle_reflect()
    print(paddle_1.distance(ball.position()))
    print(paddle_2.distance(ball.position()))

    if ball.xcor() > 500:
        score_2.score += 1
        ball.goto(0, 0)
        ball.setheading(random.choice(directions))
        score_2.update_score()

    if ball.xcor() < -500:
        score_1.score += 1
        ball.goto(random.randint(-200, 200), random.randint(-400, 400))
        ball.setheading(random.choice(directions))
        score_1.update_score()

    if ball.ycor() > 345:
        reflect()

    elif ball.ycor() < -345:
        reflect()

    time.sleep(0.1)
    update()

screen.exitonclick()
