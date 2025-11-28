from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()