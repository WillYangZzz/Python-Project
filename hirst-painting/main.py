import turtle
import random
import colorgram

# rgb_colors = []
# colors = colorgram.extract('img.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

turtle.colormode(255)
pen = turtle.Turtle()
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190),
              (40, 72, 82), (46, 73, 62), (47, 66, 82)]




# method to draw square with dots
# space --> distance between dots
# x     --> side of square
def draw(space, x):
    for i in range(x):
        for j in range(x):
            # dot
            pen.dot(20, random.choice(color_list))
            # distance for another dot
            pen.forward(space)
        pen.backward(space * x)

        # direction
        pen.right(90)
        pen.forward(space)
        pen.left(90)


# Main Section
pen.penup()
draw(60, 20)

# hide the turtle
pen.hideturtle()

screen = pen.Screen()
screen.exitonclick()
