#LAB5
#exercise1
import turtle
from turtle import *
import random

class Square(Turtle):
    def __init__(self,size, color):
        Turtle.__init__(self)
        self.size = size
        self.shape("square")
        self.shapesize(size)
        self.color(color)

    def random(self):
        self.color(random.choice(['black', 'pink', 'green', 'blue', 'orange']))

s1 = Square(5, 'pink')
s1.random_color()
