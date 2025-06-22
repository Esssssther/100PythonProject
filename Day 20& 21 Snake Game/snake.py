from turtle import Turtle
#CREATE A CONSTANT, MUST BE CAPITALIZED
MOVE_DISTANCE = 20
STARTING_POISTION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake: # first letter must be capitalized
    def __init__(self):
        self.snakeitem = []
        self.create_snake()# a method
        self.head = self.snakeitem[0]
    def create_snake(self):
        for i in STARTING_POISTION:
            self.add_segments(i)

    def add_segments(self,i):
        #add a tail to snake
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(i)  # put on the (x,y)position on the screen
        self.snakeitem.append(new_snake)

    def long(self):
        self.add_segments(self.snakeitem[-1].position())
    #move snake
    def move(self):
        for item in range(len(self.snakeitem) - 1, 0, -1):
            new_x = self.snakeitem[item - 1].xcor()
            new_y = self.snakeitem[item - 1].ycor()
            self.snakeitem[item].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # for snake_item in snake:
        # snake_item.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        #pass
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        #pass
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        #pass
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)







