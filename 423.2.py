# Problem 2

# Using the ideas from this chapter, implement a simulation of another racquet game. See the
# programming exercises from Chapter 9 for some ideas.

from random import random

class Player:
    # A player keeps track of probability of winning a serve and score

    def __init__(self, prob):
        # Create a player with this probability
        self.prob = prob
        self.score = 0

    def winsServe(self):
        return random() <= self.prob

    def incScore(self):
        self.score += 1

    def getScore(self):
        return self.score

class PingPongGame:
    # Represents a game in progress. Keeps track of which player is serving.

    def __init__(self, probA, probB):
        # Create a new game having players with the given probs.
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        # Flip a coin for serve
        if random() <= .5:
            self.server = self.playerA
            self.notServer = self.playerB
        else:
            self.server = self.playerB
            self.notServer = self.playerA

    def play(self):
        while not self.isOver():
            # update score
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.notServer.incScore()
            # change server when combined scores are even (every two points)
            if (self.playerA.getScore() + self.playerB.getScore()) % 2 == 0:
                self.changeServer()

    def isOver(self):
        a, b = self.getScores()
        return a >= 11 and a-b >= 2 or b >= 11 and b-a >= 2

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
            self.notServer = self.playerA
        else:
            self.server = self.playerA
            self.notServer = self.playerB

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()


class SimStats:
    # Tracks the wins for each player
    def __init__(self):
        self.winsA = 0
        self.winsB = 0

    def update(self, aGame):
        a, b = aGame.getScores()
        if a > b:
            self.winsA += 1
        else:
            self.winsB += 1

    def printReport(self):
        n = self.winsA + self.winsB
        print ("Summary of", n , "games:\n")
        print ("            wins (% total)")
        print ("__________________________")
        self.printLine("A", self.winsA, n)
        self.printLine("B", self.winsB, n)

    def printLine(self, label, wins, n):
        template = "Player {0}:{1:5}  ({2:5.1%})"
        print (template.format(label, wins, float(wins/n)))

def printIntro():
    print ("This program simulates n ping pong games using modern rules.")
    print ("A game is played to 11 points, with the server switching every 2 points.")
    print ("One must have a lead of at least two to win.")
    print ()

def getInputs():
    n = eval(input("How many games would you like to simulate? "))
    probA = eval(input("What is the probability that player A wins a serve? "))
    probB = eval(input("What is the probability that player B wins a serve? "))
    print ()
    return n, probA, probB

def main ():

    printIntro()

    n, probA, probB = getInputs()

    # Play the games
    stats = SimStats()
    for i in range(n):
        theGame = PingPongGame(probA, probB) # Create a new game
        theGame.play()                    # play the game
        stats.update(theGame)             # extract info

    # Print the results
    stats.printReport()




if __name__ == '__main__':
    main()
input("\nPress <Enter> to quit")