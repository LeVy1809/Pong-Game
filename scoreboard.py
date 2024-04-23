from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 40, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGN, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update()
    
    def right_point(self):
        self.right_score += 1
        self.update()