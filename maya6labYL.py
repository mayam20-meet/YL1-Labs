#lab6
from turtle import*
import random
import math

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1=Ball(300,"red",10)
ball2=Ball(200,"orange",10)

def check_collision(ball1,ball2):
    radii = ball1.radius + ball2.radius
    distance = math.sqrt(math.pow(ball2.xcor()-ball1.xcor(), 2)+ math.pow(ball2.ycor()-ball1.ycor(),2))
    if radii >= distance:
        print("collision")

    else :
        print("not collision")


ball2.goto(200,0)


