from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.right_score=0
        self.left_score=0
        self.right_and_left_score()




    def right_and_left_score(self):
        self.clear()
        self.goto(-100,260)
        self.write(self.left_score, False,"center",("Comic Sans", 30, "normal"))
        self.goto(100, 260)
        self.write(self.right_score, False, "center", ("Comic Sans", 30, "normal"))

    def update_right_score(self):
        self.right_score += 1
        self.right_and_left_score()

    def update_left_score(self):
        self.left_score += 1
        self.right_and_left_score()
