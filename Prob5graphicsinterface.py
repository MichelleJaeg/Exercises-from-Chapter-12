from graphics import *
from dieview2 import DieView
from button import Button


class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin ("Craps Game", 600, 400)
        self.win.setBackground('green3')

        banner = Text(Point(300,30), "Craps Table")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.createDice(Point(300, 100), 75)

        self.msg = Text(Point(300,275), "Welcome to the Craps Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        moneyMsg = Text(Point(280, 380), "You have:")
        moneyMsg.setSize(18)
        moneyMsg.draw(self.win)
        self.money = Text(Point(350, 380), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)
        betText = Text(Point(340, 100), 'Place a Bet:  $')
        betText.setSize(16)
        betText.draw(self.win)
        self.input = Entry(Point(460, 100), 20)
        self.input.draw(self.win)

        self.rollDiceButton = Button(self.win, Point(125, 200), 200, 40, "Roll Dice")
        self.rollDiceButton.activate()
        self.quitButton = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.quitButton.activate()
        self.helpButton = Button(self.win, Point(30, 375), 40, 30, "Help")
        self.helpButton.activate()

    def createDice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(2):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)

    def setDice(self, values):
        for i in range(2):
            self.dice[i].setValue(values[i])

    def getBetAmount(self):
        return self.input.getText()

    def showResult(self, result):
        if result == 'win':
            text = 'You won!'
        else:
            text = 'Sorry, you lost.'
        self.msg.setText(text)

    def wantToPlay(self):
        ans = self.choose()
        self.msg.setText("")
        return ans

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def choose(self):
        while True:
            p = self.win.getMouse()
            if self.rollDiceButton.clicked(p):
                return self.rollDiceButton.getLabel()
            elif self.helpButton.clicked(p):
                return self.helpButton.getLabel()
            else:
                return self.quitButton.getLabel()

    def help(self):
        helpWin = GraphWin("Help", 600, 400)
        helpWin.setBackground("blue1")

        banner = Text(Point(275, 75), "The Game of Craps:")
        banner.setSize(24)
        banner.setStyle("bold")
        banner.draw(helpWin)

        explanation = [Text(Point(305, 140), "Both dice are always rolled at the same time."),
                       Text(Point(305, 180), "A player places a bet, and then rolls the dice."),
                       Text(Point(355, 220), "A 7 or 11 on the first roll is a win, while a 2, 3, or 12 is a loss."),
                       Text(Point(285, 260), "Otherwise, the player keeps rolling until:"),
                       Text(Point(285, 300), "They re-roll their initial roll (this is a win)"),
                       Text(Point(165, 340), "Or"),
                       Text(Point(245, 380), "They roll a 7 (this is a loss)")]
        for sentence in explanation:
            sentence.draw(helpWin)
            sentence.setSize(16)
            
        closeButton = Button(helpWin, Point(60, 40), 80, 40, "Close Window")
        closeButton.activate()
        p = helpWin.getMouse()
        if closeButton.clicked(p):
            helpWin.close()

    def close(self):
        self.win.close()

    def getMouse(self):
        return self.win.getMouse()



