import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x_coordinate = self.xcor() + self.x_move
        new_y_coordinate = self.ycor() + self.y_move
        self.goto(new_x_coordinate, new_y_coordinate)

    def wall_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            # Then it needs to bounce
            self.bounce()

    def bounce(self):
        self.y_move = self.y_move * -1
        self.move()

    def paddle_bounce(self):
        self.x_move = self.x_move * -1
        self.move()

    # def ball_reset(self):
    #     pass
