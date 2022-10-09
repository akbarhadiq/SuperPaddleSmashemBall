import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()  # --> turtle.Turtle() inheritance
        self.speed(0)
        self.penup()
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        # turtle original size is 20 x 20 pixels make it so that the paddle object have width
        # of 100 pixels and length of 20 pixels
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.shape('square')
        self.goto(self.x_coordinate, self.y_coordinate)

    def up(self):
        if self.ycor() < 290:
            self.y_coordinate = self.y_coordinate + 20
            self.goto(self.x_coordinate, self.y_coordinate)

    def down(self):
        if self.ycor() > -290:
            self.y_coordinate = self.y_coordinate - 20
            self.goto(self.x_coordinate, self.y_coordinate)
