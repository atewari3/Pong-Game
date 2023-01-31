from turtle import Turtle,Screen


class Paddle(Turtle):
    def __init__(self,cord):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(5,0.7)
        self.setposition(cord)

    def move_up(self):
        new_y = self.ycor() + 23
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 23
        self.goto(self.xcor(), new_y)
