from diceForCraps import Dice

class CrapsApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self. interface = interface

    def run(self):
        while self.money >= 0:
            choice = self.interface.wantToPlay()
            if choice == "Roll Dice":
                self.playRound()
            elif choice == "Help":
                self.interface.help()
            elif choice == "Quit":
                break
        # close window
        self.interface.close()

    def playRound(self):
        self.rollDice()
        initialRoll = self.dice.rollNumber()
        betAmount = self.interface.getBetAmount()
        betAmount = int(betAmount)

        if initialRoll == 7 or initialRoll == 11:
            result = 'win'
            self.interface.showResult(result)

        elif initialRoll == 2 or initialRoll == 3 or initialRoll == 12:
            result = 'loss'
            self.interface.showResult(result)

        else:
            while True:
                self.interface.msg.setText("Please roll again.")
                p = self.interface.getMouse()
                if self.interface.rollDiceButton.clicked(p):
                    self.rollDice()
                number = self.dice.rollNumber()
                self.interface.setDice(self.dice.values())
                if number == initialRoll:
                    result = 'win'
                    self.interface.showResult('win')
                    break
                elif number == 7:
                    result = 'loss'
                    self.interface.showResult('loss')
                    break

        if result == 'win':
            self.money = self.money + betAmount
        elif result == 'loss':
            self.money = self.money - betAmount

        self.interface.setMoney(self.getMoney())

    def rollDice(self):
        self.dice.rollAll()
        self.interface.setDice(self.dice.values())

    def getMoney(self):
        return self.money



