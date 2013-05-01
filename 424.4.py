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

        # inform user incorrect information entered
        win.incorrectInput()

    # close window and continue if correct info entered
    win.close()

    while True:

        # open the next window
        optionsWin = OptionsWindow()

        # Convert ints to strings
        checkingbalance = customer.getChecking()
        checkingbalance = int(checkingbalance)
        if 1000 <= checkingbalance <= 10000:
            cbStr = str(checkingbalance)
            checkingbalance =  '$' + cbStr[0] + ',' + cbStr[1] + cbStr[2] + cbStr[3]
        elif checkingbalance < 1000:
            checkingbalance = '$' + str(checkingbalance)
        else:
            cbStr = str(checkingbalance)
            checkingbalance = '$' + cbStr[0] + cbStr[1] + ',' + cbStr[2] + cbStr[3]\
            + cbStr[4]
        savingsbalance = customer.getSavings()
        savingsbalance = int(savingsbalance)
        if 1000 <= savingsbalance <= 10000:
            cbStr = str(savingsbalance)
            savingsbalance =  '$' + cbStr[0] + ',' + cbStr[1] + cbStr[2] + cbStr[3]
        elif savingsbalance < 1000:
            savingsbalance = '$' + str(savingsbalance)
        else:
            cbStr = str(savingsbalance)
            savingsbalance = '$' + cbStr[0] + cbStr[1] + ',' + cbStr[2] + cbStr[3]\
            + cbStr[4]

        # User chooses from three options and chooses checking or savings
        action, account  = optionsWin.choose(checkingbalance, savingsbalance)
        optionsWin.close()
        if account == 'From Checking':
            balance = checkingbalance
        elif account == 'From Savings':
            balance = savingsbalance

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
            choice = win.choose()
            if choice == "$20":
                amount = 20
            elif choice == "$40":
                amount = 40
            elif choice == "$60":
                amount = 60
            elif choice == "$80":
                amount = 80
            elif choice == "$100":
                amount = 100
            elif choice == "$200":
                amount = 200
            elif choice == "$500":
                amount = 500
            elif choice == "$1,000":
                amount = 1000
            if balance == checkingbalance:
                customer.withdrawFromChecking(amount)
            elif balance == savingsbalance:
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
            amount.strip(',')
            amount = int(amount)

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