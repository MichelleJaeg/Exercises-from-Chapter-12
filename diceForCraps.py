from random import randrange

class Dice:
    def __init__(self):
        self.dice = [0]*2
        self.rollAll()

    def roll(self, which):
         for pos in which:
             self.dice[pos] = randrange(1,7)

    def rollAll(self):
        for dice in self.dice:
            self.roll(range(2))
        return self.dice

    def values(self):
        return self.dice[:]

    def rollNumber(self):
        counter = 0
        for dice in self.dice:
            counter += dice
        return counter
