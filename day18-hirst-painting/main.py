# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_rgb_list = []
# for i in range(30):
#     rgb = colors[i].rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color_tuple = (r, g, b)
#     color_rgb_list.append(color_tuple)
# print(color_rgb_list)
import random
import turtle as t
t.colormode(255)
colors = [(198, 166, 115), (141, 76, 56), (234, 237, 242), (240, 245, 241), (62, 91, 118), (219, 202, 144), (151, 147, 70), (123, 41, 30), (139, 161, 182), (60, 110, 81), (67, 48, 41), (190, 99, 78), (151, 176, 148), (156, 144, 157), (226, 178, 168), (100, 76, 78), (90, 143, 127), (52, 47, 50), (46, 59, 68), (185, 204, 176), (51, 64, 79), (39, 81, 84), (39, 82, 74), (112, 126, 147), (179, 191, 207), (101, 41, 44), (67, 63, 59), (168, 94, 97)]
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
original_position = tim.position()
for j in range(10):
    for i in range(10):
        tim.pendown()
        tim.dot(20,random.choice(colors))
        tim.penup()
        current_position = tim.position()
        tim.goto(current_position[0]+30,current_position[1] )
    tim.goto(original_position[0], current_position[1]+30)




screen = t.Screen()
screen.exitonclick()