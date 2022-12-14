from turtle import Turtle
FONT = ("Courier", 24, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align = 'center', font=FONT)

    def levell(self):
        self.level += 1
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", font=FONT)

