from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scorenum = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score = {self.scorenum}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scorenum +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
