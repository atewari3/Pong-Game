from turtle import Turtle


class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.width(7)
        self.color("white")
        self.setheading(270)
        self.goto(0, 300)
        for i in range(1,13):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
