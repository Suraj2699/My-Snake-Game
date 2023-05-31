from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision With Food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.clear()
        scoreboard.scoreupdate()

    # Detect Collision With Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_is_on = False

    # Detect Collision With Tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # If head collides with any segment of tail:
        # Trigger Game Over


    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

screen.exitonclick()
