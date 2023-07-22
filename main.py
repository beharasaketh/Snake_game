import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_Score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
#     detect collisons with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
















screen.exitonclick()