import turtle
from turtle import Turtle, Screen
import random
from tkinter import messagebox

screen = Screen()

#screen size is crucial in this game, so we set up a screen size
screen.setup(width=500, height=400)#keywords arguement
is_race_on = False
#bring up a pop to ask user for bet which turtle will win
#Pop up a dialog window for input of a string
#turtle.textinput(title, prompt)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win the race? Enter a color:")
print(user_bet)
all_turtles = []
colors = ["red","orange","yellow","green","blue","purple"]
for i in range(0,6):
#set the turtle start at the left edge of the screen
#in every loop, created a new object, independent, instance
    new_turtle = Turtle(shape="turtle") #create a object with a shape of turtle
#if the center is 0,0, height = 400, width = 500

    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y= i*50 -100) #put on the (x,y)position on the screen
    new_turtle.pendown()
    all_turtles += [new_turtle] #or like all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtleinstance in all_turtles:

        if turtleinstance.xcor() > 230:
            is_race_on = False
            winning_color = turtleinstance.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo(title="Result",message=f"You've won! The {winning_color} turtle is the winner")
                #print(f"You've won! The {winning_color} turtle is the winner")
            else:
                messagebox.showinfo(title="Result", message=f"You've lost! The {winning_color} turtle is the winner")
                #print(f"You've lost! The {winning_color} turtle is not the winner")
        random_distance = random.randint(0, 10)
        turtleinstance.forward(random_distance)

screen.exitonclick()