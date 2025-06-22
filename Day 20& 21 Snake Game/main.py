from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)  # until we call update, the screem will remain unupdated

snake = Snake()  # use snake class
food = Food()
score = Score()

screen.listen()
# arrow key on the key board in python can be call Up, Down, Right, Left
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")  # method first and key later
screen.onkey(snake.left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # screen sleep 1 second after each item move and screen update
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.long()

    #Detect collison with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False
    #if head collides with any segment in the tail: trigger game over

    for snakeitem in snake.snakeitem[1:]:
        #everything other than first item, the head itself
        if snake.head.distance(snakeitem) < 10 :
            score.game_over()
            game_is_on = False

screen.exitonclick()
