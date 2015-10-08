__author__ = 'Isaiah'
from random import random


class game:
    def play(self, team1, team2):
        if team1.skill > team2.skill:
            self.winner = 1
            team1.win()
            team1.lose()
        elif team2.skill > team1.skill:
            self.winner = 2
            team2.win()
            team1.lose()
        else:
            self.winner = 3
            if random() > .5:
                team1.win()
                team2.lose()
            else:
                team2.win()
                team1.lose()

    def __init__(self, team1, team2):
        self.winner = 0
        self.play(team1, team2)
