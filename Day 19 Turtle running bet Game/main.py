from turtle import Turtle, Screen

tim = Turtle()
screen = Screen() #use it by create a object


def move_forwards():
    tim.forward(10)

def move_backwords():
    tim.backward(10)
def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forwards) #not use ()  here behind the function
screen.onkey(key="s",fun=move_backwords)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
#pass function as import to another function, function_a(function_b) here b function do not have ()

#W = forward, S= backwords, A= counter-clockwise, D = clockwise, C= clear_drawing

