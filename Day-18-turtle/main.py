import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

# for _ in range(150):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r,g,b)
#
# directions = [0, 90, 180, 270]
#
tim.pensize(3)
tim.speed("fastest")
#
# for i in range(200):
#   tim.forward(30)
#   tim.setheading(random.choice(directions))
#   color = random_color()
#   tim.color(color)
def draw_direction(size_of_gap):
  for i in range(int(360/ size_of_gap)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)
draw_direction(5)









screen = Screen()
screen.exitonclick()