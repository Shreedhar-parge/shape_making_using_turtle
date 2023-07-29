from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["red", "blue", "green", "black", "yellow", "pink", "orange"]


def draw_shap(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colours))
    draw_shap(shape_side)


screen = Screen()
screen.exitonclick()