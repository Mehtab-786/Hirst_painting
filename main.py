"""
# way to extract colours from an image
import colorgram
colors = colorgram.extract("DHS4591_771_0.jpg",23)

rgb =[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    name = (r,g,b)
    rgb.append(name)

 print(rgb)"""
import random
import turtle
from turtle import Turtle, Screen

rgb_colors = [(182, 65, 34), (213, 149, 97), (14, 24, 42),  (239, 208, 94), (237, 62, 33), (157, 26, 19), (72, 29, 32),
              (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127),
              (229, 175, 161), (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165)]


turtle.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.setposition(-200, -220)
tim.pendown()
tim.speed(0)
a = 1


while a < 11:
    for i in range(10):
        tim.color(random.choice(rgb_colors))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    a += 1

screen = Screen()
screen.exitonclick()
