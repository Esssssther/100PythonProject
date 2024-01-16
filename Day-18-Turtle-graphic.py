import random
from turtle import Turtle, Screen, colormode

# import turtle as t
# tim=t.Turtle()
tim = Turtle()
colormode(255)
# https://docs.python.org/3/library/turtle.html
# stack overflow
# timmy_the_turtle.shape("turtle")
# draw a square
tim.shape("arrow")
# Return the current pencolor and the current fillcolor as a pair of color specification strings or tuples
# timmy_the_turtle.color("purple")
tim.pencolor("#8B4513")
tim.fillcolor("#F5DEB3")
for i in range(4):
    tim.right(90)
    tim.forward(100)

# show screen and exit on click to quit
screen = Screen()

screen.reset()
# draw dash
tim.shape("arrow")
tim.color("black")
for i in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


#  spirograph
screen.reset()
tim.speed("normal")


def draw_spirograph(size_of_gap):
    for direction in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(50)
        # tim. right(10)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(20)

# draw different shapes
screen.reset()
tim.shape("arrow")
# color = ["red", "blue", "purple", "green", "brown", "black", "dark green", "medium aquamarine", "deep pink"]
for i in range(3, 11):
    #    tim.color(random.choice(color))
    tim.color(random_color())
    for j in range(i):
        tim.forward(100)
        tim.right(360 / i)
    tim.home()

#  random walk
screen.reset()
angle = [90, 180, 270, 0]
speed = 1
width = 1
for move in range(200):
    if speed == 10 or speed == 0:
        speed = 0
    else:
        speed += 0.1
    tim.speed(speed)  # from slow to fastest
    tim.pensize(width)
    tim.color(random_color())
    # tim.color(random.choice(color))
    tim.setheading(random.choice(angle))
    tim.forward(20)
    width += 0.1  # more thick during the draw
# tuple does not support item assignment (change item)
# immutable
# color r,g,b, 0-255

screen.exitonclick()
