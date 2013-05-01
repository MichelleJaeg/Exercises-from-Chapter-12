# This class provided by textbook (except for help button/method)

from graphics import*
from button import Button
from dieview2 import DieView


class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")

        banner = Text(Point(300,30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)

        self.createDice(Point(300, 100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        
        # Create Help button
        b = Button(self.win, Point(30, 375), 40, 30, "Help")
        self.buttons.append(b)
        b.activate()

        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit", "Help"])
        self.msg.setText("")
        return ans

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices= []
        while True:
            # wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score"])

            if b[0] == "D":             # User clicked a die button
                i = eval(b[4]) -1     # Translate label to the die index
                if i in choices:        # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:                  # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                                      # User clicked Roll or Score
                for d in self.dice:   # Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":      # Score clicked, ignore choices
                    return []
                elif choices !=[]:    # Don't accept Roll unless some
                    return choices    #    dice are actually selected

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() # function exit here.

    def help(self):
        helpWin = GraphWin("Help", 600, 400)
        helpWin.setBackground("blue")
        rulesText = Text(Point(300, 30), "Rules of the Game:")
        rulesText.setSize(24)
        rulesText.draw(helpWin)
        rules = [Text(Point(290, 100), "A player starts with $100. Each round costs $10 to play."),
                 Text(Point(230, 140), "A player initially roles a random hand."),
                 Text(Point(300, 180), "Dice can be re-rolled up to two times (any number of dice)."),
                 Text(Point(165, 240), "Payout Schedule:")]
        for rule in rules:
            rule.draw(helpWin)
            rule.setSize(16)
        payouts = [Text(Point(165, 280), "Two Pairs, $5"),
                   Text(Point(170, 300), "Three of a Kind, $8"),
                   Text(Point(165, 320), "Full House, $12"),
                   Text(Point(170, 340), "Four of a Kind, $15"),
                   Text(Point(165, 360), "Straight, $20"),
                   Text(Point(170, 380), "Five of a Kind, $30")]
        for item in payouts:
            item.draw(helpWin)
            item.setSize(16)

        closeButton = Button(helpWin, Point(60, 40), 80, 40, "Close Window")
        closeButton.activate()
        p = helpWin.getMouse()
        if closeButton.clicked(p):
            helpWin.close()

    def inputNameHighScore(self):
        highScoreWin = GraphWin("HighScore!", 600, 400)
        highScoreWin.setBackground("blue")
        highScoreMsg = Text(Point(300, 125), "You got a high score!")
        highScoreMsg.setSize(24)
        highScoreMsg.draw(highScoreWin)
        inputMsg = Text(Point(150, 250), "Please enter your name with no spaces:")
        inputMsg.setSize(16)
        inputMsg.draw(highScoreWin)
        input = Entry(Point(400, 250), 35)
        input.draw(highScoreWin)
        enterButton = Button(highScoreWin, Point(350, 325), 45, 30, "Enter")
        enterButton.activate()
        highScoreWin.getMouse()
        name = input.getText()
        highScoreWin.close()
        return name

    def close(self):
        self.win.close()
