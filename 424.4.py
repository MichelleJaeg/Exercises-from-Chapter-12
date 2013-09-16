# Problem 4

# Write a program that simulates an ATM

from Prob4graphicsinterface import IntroWindow, OptionsWindow, CheckBalancesWindow
from Prob4graphicsinterface import WithdrawWindow, TransferWindow, ExitWindow

class Customer:
    def __init__(self, name, username, pin, checking, savings):
        self.name = name
        self.username = username
        self.pin = pin
        self.checking = int(checking)
        self.savings = int(savings)

    def getName(self):
        return self.name

    def getUserName(self):
        return self.username

    def getPin(self):
        return self.pin

    def getChecking(self):
        return self.checking

    def getSavings(self):
        return self.savings

    def withdrawFromChecking(self, amount):
        self.checking = self.getChecking() - amount

    def withdrawFromSavings(self, amount):
        self.savings = self.getSavings() - amount

    def addToChecking(self, amount):
        self.checking = self.getChecking() + amount

    def addToSavings(self, amount):
        self.savings = self.getSavings() + amount

def makeList():
    infile = open('infoForATMProgram', "r")
    myList = []
    for line in infile:
        items = line.split()
        name = items[0]
        username = items[1]
        pin = items[2]
        checking = items[3]
        savings = items[4]
        person = Customer(name, username, pin, checking, savings)
        myList.append(person)
    return myList

def ints_to_Strings(number):
        return "${0:0.2f}".format(number)

def main ():

    # Make intro window
    win = IntroWindow()

    correctInfo = False
    myList = makeList()
    while not correctInfo:

        # check for match
        username, pin = win.getInputs()
        for person in myList:
            if username == person.getUserName() and pin == person.getPin():
                correctInfo = True
                customer = person
                break

        # inform user incorrect information entered
        if not correctInfo:
            win.incorrectInput()

    # close window and continue if correct info entered
    win.close()

    while True:

        # open the next window
        optionsWin = OptionsWindow()

        # Convert ints to strings
        checkingBalance = ints_to_Strings(customer.getChecking())
        savingsBalance = ints_to_Strings(customer.getSavings())

        # User chooses from three options and chooses checking or savings
        action, account  = optionsWin.choose(checkingBalance, savingsBalance)
        optionsWin.close()
        if account == 'From Checking':
            balance = checkingBalance
        elif account == 'From Savings':
            balance = savingsBalance

        # if user chooses check balances
        if action == 'Check Balances':
             win = CheckBalancesWindow(balance)
             choice = win.choose()
             if choice == 'Exit':
                 win.close()
                 break
             else:
                 win.close()

        # if user chooses withdraw cash
        elif action == 'Withdraw Cash':
            win = WithdrawWindow()
            # user chooses amount to withdraw
            # get rid of dollar signs and commas, and convert to int
            choice = win.choose()
            amount = int(choice.strip("$").strip(","))
            if balance == checkingBalance:
                customer.withdrawFromChecking(amount)
            elif balance == savingsBalance:
                customer.withdrawFromSavings(amount)
             # After withdrawing cash
            win.close()
            exitWin = ExitWindow()
            choice = exitWin.choose()
            if choice == 'Exit':
                exitWin.close()
                break
            else:
                exitWin.close()

        # if user chooses transfer money
        elif action == 'Transfer Money':
            win = TransferWindow()

            # direction of transfer
            type = win.choose()
            # amount to transfer
            amount = win.input.getText()
            amount = int(amount.strip("$").strip(","))

            if type == 'From checking to savings':
                customer.withdrawFromChecking(amount)
                customer.addToSavings(amount)

            elif type == 'From savings to checking':
                customer.withdrawFromSavings(amount)
                customer.addToChecking(amount)

            # After transferring money
            win.close()
            exitWin = ExitWindow()
            choice = exitWin.choose()
            if choice == 'Exit':
                exitWin.close()
                break
            else:
                exitWin.close()

    # write changes to file
    outfile = open('infoForATMProgram', 'w')
    for customer in myList:
        name = customer.getName()
        username = customer.getUserName()
        pin = customer.getPin()
        checking = customer.getChecking()
        savings = customer.getSavings()
        print (name, username, pin, checking, savings, file=outfile)
    outfile.close()


if __name__ == '__main__':
    main ()