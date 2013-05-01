# This class provided by textbook (except for changes/methods related to the help button and
# high score feature)


from dice import Dice

class PokerApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self. interface = interface

    def run(self):
        while self.money >= 10:
            choice = self.interface.wantToPlay()
            if choice == "Roll Dice":
                self.playRound()
            elif choice == "Help":
                self.interface.help()
            elif choice == "Quit":
                #Figure out if high score
                score = self.getMoney()
                if self.isHighScore():
                    # Change list
                    self.removePerson()
                    list = self.addPerson()
                    # Print info to file to save for next time
                    self.printToFile(list)
                # close window
                self.interface.close()
                break
        # close window
        self.interface.close()

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll +1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

    def getMoney(self):
        return self.money

    def makeScoreList(self):
        scoreList = []
        infile = open("HighScores", 'r')
        for line in infile:
            name, score = line.split()
            tuple = (name, score)
            scoreList.append(tuple)
        return scoreList

    def isHighScore(self):
        newScore = self.getMoney()
        list = self.makeScoreList()
        flag = False
        if len(list) == 10:
            for tuple in list:
                score = int(tuple[1])
                if newScore > score:
                    flag = True
        else:
            flag = True
        return flag

    def addPerson(self):
        score = self.getMoney()
        name = self.interface.inputNameHighScore()
        tuple = (name, score)
        list = self.removePerson()
        list.append(tuple)
        return list

    def removePerson(self):
        list = self.makeScoreList()
        if len(list) == 10:
            trackerNumber = 10000
            trackerTuple = None
            for tuple in list:
                score = int(tuple[1])
                if score < trackerNumber:
                    trackerNumber = score
                    trackerTuple = tuple
            list.remove(trackerTuple)
        return list

    def printToFile(self, list):
        outfile = open('HighScores', 'w')
        for tuple in list:
            name, score = tuple
            print (name, score, file = outfile)
        outfile.close()





