from turtle import Turtle, Screen



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"score: {self.score}", align="center", font= ('Arial', 22, 'normal'))
        self.hideturtle()

    def update_Score(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", align="center", font= ('Arial', 22, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_Score()

    def increase_Score(self):
        self.score += 1
        self.update_Score()



