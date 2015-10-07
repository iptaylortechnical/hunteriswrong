__author__ = 'Isaiah'


class team:
    def win(self):
        for p in self.players:
            p.playedGame(True)
            p.assignTeam(0)

    def lose(self):
        for p in self.players:
            p.playedGame(False)
            p.assignTeam(0)

    def findAverage(self):
        count = 0
        for t in self.players:
            count += t.skill
        return count/len(self.players)

    def __init__(self, players):
        self.players = players
        self.skill = self.findAverage()