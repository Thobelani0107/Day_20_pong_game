from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.increase_speed=0.1
        self.x_value=10
        self.y_value=10


    def move(self):
        new_x= self.xcor()+self.x_value
        new_y=self.ycor()+self.y_value
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_value*=-1
        self.increase_speed*=0.9


    def bounce_x(self):
        self.x_value*=-1
        self.increase_speed *= 0.9

    def reset(self):
        self.increase_speed=0.1
        self.goto(0,0)
        self.bounce_x()

