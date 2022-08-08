#making the different shape using the turtle
import random
from turtle import Turtle,Screen
import random

tom = Turtle()

#prodiving the list of colours
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "black", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)


for shape_side_n in range(3, 11):
    tom.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()

