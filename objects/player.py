__author__ = 'Isaiah'
from random import random


class player:
    def assignTeam(self, team):
        self.currentTeam = team

    def playedGame(self, won):
        self.gamesPlayed += 1
        if won:
            self.gamesWon += 1
        else:
            self.gamesLost += 1

    def __init__(self, ind):
        self.ind = ind
        self.skill = int(random()*10)
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.gamesLost = 0
        self.currentTeam = 0