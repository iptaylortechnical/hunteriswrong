__author__ = 'Isaiah'


class team:
    def win(self):
        for p in self.players:
            p.playedGame(True)

    def lose(self):
        for p in self.players:
            p.playedGame(False)

    def findAverage(self):
        count = 0
        for t in self.players:
            count += t.skill
        return count/len(self.players)

    def __init__(self, players):
        self.players = players
        self.skill = self.findAverage()