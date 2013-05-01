from graphics import*
from button import Button

class IntroWindow:
    def __init__(self):
        self.IntroWin = GraphWin("WELCOME", 600, 400)
        self.IntroWin.setBackground("blue")

        banner = Text(Point(290, 65), "Welcome To BankName")
        banner.setSize(32)
        banner.setStyle("bold")
        banner.draw(self.IntroWin)

        self.IDmsg = Text(Point(150, 150), "Please enter your user ID:")
        self.IDmsg.setSize(16)
        self.IDmsg.draw(self.IntroWin)

        self.input1 = Entry(Point(380, 150), 35)
        self.input1.draw(self.IntroWin)

        self.pinMsg = Text(Point(155, 250), "Please enter your pin number:")
        self.pinMsg.setSize(16)
        self.pinMsg.draw(self.IntroWin)

        self.input2 = Entry(Point(385, 250), 35)
        self.input2.draw(self.IntroWin)

        self.EnterButton = Button(self.IntroWin, Point(550, 250), 50, 60, 'Enter')
        self.EnterButton.activate()

    def getInputs(self):
        p = self.IntroWin.getMouse()
        if self.EnterButton.clicked(p):
            username = self.input1.getText()
            pin = self.input2.getText()
        return username, pin

    def incorrectInput(self):
        msg = Text(Point(290, 325), "*Incorrect username or pin number")
        msg.setSize(24)
        msg.setStyle('bold')
        msg.draw(self.IntroWin)

    def close(self):
        self.IntroWin.close()

class OptionsWindow:
    def __init__(self):
        self.OptionsWin = GraphWin("BankName", 600, 400)
        self.OptionsWin.setBackground("blue")

        banner = Text(Point(290, 50), "Please select a transaction")
        banner.setSize(24)
        banner.setStyle("bold")
        banner.draw(self.OptionsWin)

        self.buttons = []
        bSpecs = [(175, 125, 'Check Balances'), (175, 225, 'Withdraw Cash'),
                  (175, 325, "Transfer Money")]
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.OptionsWin, Point(cx, cy), 100, 50, label))
        for b in self.buttons:
            b.activate()
        self.buttons2 = []
        bSpecs2 = [(400, 160, 'From Checking'), (400, 310, 'From Savings')]
        for (cx, cy, label) in bSpecs2:
            self.buttons2.append(Button(self.OptionsWin, Point(cx, cy), 150, 75, label))
        for b in self.buttons2:
            b.activate()

    def choose(self, checkingBalance, savingsBalance):
        p = self.OptionsWin.getMouse()
        for b in self.buttons:
            if b.clicked(p):
                x =  b.getLabel()
        p = self.OptionsWin.getMouse()
        for b in self.buttons2:
            if b.clicked(p):
                y = b.getLabel()
        return x, y

    def close(self):
        self.OptionsWin.close()

class CheckBalancesWindow:
    def __init__(self, balance):
        # Show balance
        self.BalancesWin = GraphWin("Balance", 600, 400)
        self.BalancesWin.setBackground("blue")
        self.balance = balance
        self.buttons = []
        self.balanceMsg = Text(Point(250, 80),"Your balance is: ")
        self.balanceMsg.setSize(24)
        self.balanceMsg.draw(self.BalancesWin)
        self.balance = Text(Point(400, 80), self.balance)
        self.balance.setSize(24)
        self.balance.draw(self.BalancesWin)

        # User chooses to exit or make another transaction
        bSpecs = [(150, 250, 'Make another transaction'), (450, 250, 'Exit')]
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.BalancesWin, Point(cx, cy), 175, 50, label))
        for b in self.buttons:
            b.activate()

    def choose(self):
        p = self.BalancesWin.getMouse()
        for b in self.buttons:
            if b.clicked(p):
                choice = b.getLabel()
        return choice

    def close(self):
        self.BalancesWin.close()

class WithdrawWindow:
    def __init__(self):
        self.WithdrawWin = GraphWin("Withdrawal", 600, 400)
        self.WithdrawWin.setBackground("blue")
        self.buttons = []

        self.amountMsg = Text(Point(300, 50), "How much would you like to withdraw?")
        self.amountMsg.setSize(24)
        self.amountMsg.draw(self.WithdrawWin)

        bSpecs = [(150, 150, '$20'), (150, 250, '$40'), (150, 350, '$60'),
                  (300, 150, '$80'), (300, 250, '$100'), (300, 350, '$200'),
                  (450, 150, '$500'), (450, 250, '$1,000')]
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.WithdrawWin, Point(cx, cy), 100, 75, label))
        for b in self.buttons:
            b.activate()

    def choose(self):
        p = self.WithdrawWin.getMouse()
        for b in self.buttons:
            if b.clicked(p):
                choice = b.getLabel()
        return choice

    def close(self):
        self.WithdrawWin.close()

class TransferWindow:
    def __init__(self):
        self.TransferWin = GraphWin("Transfer Money", 600, 400)
        self.TransferWin.setBackground("blue")

        banner = Text(Point(300, 80),"Choose an Option Below: ")
        banner.setSize(32)
        banner.setStyle("bold")
        banner.draw(self.TransferWin)
        self.buttons = []

        bSpecs = [(200, 300, 'From checking to savings'), (400, 300, 'From savings to checking')]
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.TransferWin, Point(cx, cy), 175, 50, label))
        for b in self.buttons:
            b.activate()

        self.amountMsg = Text(Point(225, 200), "Amount: ")
        self.amountMsg.setSize(16)
        self.amountMsg.draw(self.TransferWin)
        self.input = Entry(Point(340, 200), 25)
        self.input.draw(self.TransferWin)

    def choose(self):
        p = self.TransferWin.getMouse()
        for b in self.buttons:
            if b.clicked(p):
                choice = b.getLabel()
        return choice

    def close(self):
        self.TransferWin.close()

class ExitWindow:
    def __init__(self):
        self.ExitWin = GraphWin("Goodbye!", 600, 400)
        self.ExitWin.setBackground("blue")
        self.buttons = []
        bSpecs = [(150, 200, 'Make another transaction'), (450, 200, 'Exit')]
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.ExitWin, Point(cx, cy), 175, 50, label))
        for b in self.buttons:
            b.activate()

    def choose(self):
        p = self.ExitWin.getMouse()
        for b in self.buttons:
            if b.clicked(p):
                choice = b.getLabel()
        return choice

    def close(self):
        self.ExitWin.close()





