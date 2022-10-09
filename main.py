import turtle
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen Setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("SuperPaddleSmashemBall")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

# Right Paddle
paddle1 = Paddle(x_coordinate=350, y_coordinate=0)
# Paddle Key Screen Listener
screen.onkeypress(key='Up', fun=paddle1.up)
screen.onkeypress(key='Down', fun=paddle1.down)

# Left Paddle
paddle2 = Paddle(x_coordinate=-350, y_coordinate=0)
# Paddle Key Screen Listener
screen.onkeypress(key='w', fun=paddle2.up)
screen.onkeypress(key='s', fun=paddle2.down)

# Ball
ball = Ball()

# Right Paddle Score:   # --> Coordinate for right paddle is (200, 280)
r_paddle_scoreboard_xy_coordinates = (200, 260)
right_paddle_score = Scoreboard(r_paddle_scoreboard_xy_coordinates)

# Left Paddle Score
l_paddle_scoreboard_xy_coordinates = (-200, 260)
left_paddle_score = Scoreboard(l_paddle_scoreboard_xy_coordinates)


# Midfield Separator Lines ##########################
def separator():
    separator_lines = turtle.Turtle()
    separator_lines.goto(0, 600)
    separator_lines.seth(270)
    # separator_lines.hideturtle()
    separator_lines.color('white')
    for _ in range(31):
        separator_lines.forward(10)
        separator_lines.penup()
        separator_lines.forward(10)
        separator_lines.pendown()
        separator_lines.forward(10)


#######################################################

game_is_on = True

separator()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    print(f" Ball X Coordinates :{ball.xcor()}")
    print(f" Ball Y Coordinates :{ball.ycor()}")
    # Detect Ball Collision
    ball.wall_collision()

    # Detect Paddle Collision
    # --> Right Paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 330:
        ball.paddle_bounce()

    # --> Left Paddle
    if ball.distance(paddle2) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    # Detect when right paddle misses:
    if ball.xcor() > 350:
        # Resets ball and Reverses X axis ball course
        ball.goto(0, 0)
        ball.x_move = ball.x_move * -1
        # Increase right player paddle score
        right_paddle_score.increase_score()

    # Detect when the left paddle misses:
    if ball.xcor() < -350:
        # Resets ball and Reverses X axis ball course
        ball.goto(0, 0)
        ball.x_move = ball.x_move * -1
        # Increase left paddle player score
        left_paddle_score.increase_score()

screen.exitonclick()
