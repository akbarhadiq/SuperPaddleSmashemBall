import turtle
FONT = ("Arial", 12, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self, xy_coordinates):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(xy_coordinates)
        self.write(f"Score\n    {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.undo()
        self.write(f"Score\n    {self.score}", align="center", font=FONT)
