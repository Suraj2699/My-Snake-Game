from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(270)
        self.color("white")
        self.hideturtle()
        self.write("Score: 0", False, align=ALIGNMENT, font=FONT)

        self.score = 0

    def scoreupdate(self):
        self.score += 1
        self.write("Score: " + str(self.score), False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
