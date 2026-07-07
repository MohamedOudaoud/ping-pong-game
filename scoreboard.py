from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()
    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,230)
        self.write(f"{self.l_score}        {self.r_score}", align="center", font=("arial", 40, "normal"))
