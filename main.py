# import colorgram
#
# rgb_colors=[]
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r,g,b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
import turtle
import turtle as t
import random

t.colormode(255)
color_list = [(173, 51, 76), (119, 159, 199), (211, 221, 229), (41, 91, 140), (217, 145, 98), (205, 73, 101), (66, 115, 57), (224, 153, 17), (119, 191, 152), (225, 232, 227), (47, 164, 106), (15, 65, 140), (218, 81, 66), (205, 134, 177), (138, 100, 79), (140, 29, 36), (211, 200, 101), (44, 43, 71), (210, 180, 211), (168, 192, 223), (157, 204, 220), (49, 72, 57), (46, 66, 53), (67, 181, 184), (132, 33, 31), (123, 121, 162), (172, 204, 187), (225, 176, 169)]
tim = t.Turtle()

tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
