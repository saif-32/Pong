from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_value = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1

    def paddle_collision(self):
        self.x_move *= -1
        self.speed_value *= 0.9

    def reset_position(self):
        self.home()
        self.speed_value = 0.1
        self.paddle_collision()