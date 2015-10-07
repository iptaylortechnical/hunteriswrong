__author__ = 'Isaiah'
from objects import game, player

class engine:
    def newGame(self, users, games, slots):
        userB = []
        for u in range(users):
            userB[u] = player(u)


    def __init__(self, users, games, slots):
        if not users % slots == 0:
            raise ValueError("users and slots not divisible")
        self.newGame(users, games, slots)