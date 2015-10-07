__author__ = 'Isaiah'
from objects import game, player, team
from random import random


class engine:
    def newGame(self, users, games, slots):
        userB = []
        for u in range(users):
            userB[u] = player.player(u)
        for g in range(games):
            team1arr = []
            team2arr = []
            for o in range(slots):
                while True:
                    randIndex1 = int(random()*slots)
                    if userB[randIndex1].gamesPlayed < games and userB[randIndex1].currentTeam == 0:
                        userB[u].assignTeam(1)
                        team1arr[o] = userB[u]
                        break
                while True:
                    randIndex2 = int(random()*slots)
                    if userB[randIndex2].gamesPlayed < games and userB[randIndex2].currentTeam == 0:
                        userB[u].assignTeam(2)
                        team2arr[o] = userB[u]
                        break
            team1 = team.team(team1arr)
            team2 = team.team(team2arr)
            game.game(team1, team2)

    def __init__(self, users, games, slots):
        if not users % slots == 0:
            raise ValueError("users and slots not divisible")
        self.newGame(users, games, slots)