__author__ = 'Isaiah'
from objects import game, player, team
from random import random


class engine:
    def newGame(self, users, games, slots):
        userB = []
        for u in range(users):
            userB.append(player.player(u))
        for g in range(games):
            team1arr = []
            team2arr = []
            print('meh')
            for o in range(slots):
                while True:
                    randIndex1 = int(random()*users)
                    if len(team1arr) < slots:
                        if userB[randIndex1].gamesPlayed < games and userB[randIndex1].currentTeam == 0:
                            userB[randIndex1].assignTeam(1)
                            team1arr.append(userB[randIndex1])
                            break
                    else:
                        break
                while True:
                    randIndex2 = int(random()*users)
                    if len(team2arr) < slots:
                        if userB[randIndex2].gamesPlayed < games and userB[randIndex2].currentTeam == 0:
                            userB[randIndex2].assignTeam(2)
                            team2arr.append(userB[randIndex2])
                            break
                    else:
                        break
                print(len(team1arr), len(team2arr))
            team1 = team.team(team1arr)
            team2 = team.team(team2arr)
            g = game.game(team1, team2)
            print('g', g.winner)
        w = 0
        for b in userB:
            b.calculateWR()
            w += b.WR

    def __init__(self, users, games, slots):
        if not users % slots == 0:
            raise ValueError("users and slots not divisible")
        self.newGame(users, games, slots)