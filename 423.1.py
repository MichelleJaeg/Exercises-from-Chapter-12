# Problem 1

# Modify the Dice Poker program from this chapter to include any or all of the following features:
# Add a splash screen, add a help button, add a high scores feature


from pokerapp import PokerApp
from graphicsinterface import GraphicsInterface
from button import Button
from graphics import*
from dieview2 import DieView

def splashScreen():
    firstWin = GraphWin("Dice Poker", 600, 400)
    firstWin.setBackground("blue")

    die = DieView(firstWin, Point(80,180), 100)
    die.setValue(4)
    die2 = DieView(firstWin, Point(520, 270), 100)
    die2.setValue(6)

    TitleMessage = Text(Point(210, 40), "Dice Poker:")
    TitleMessage.setSize(32)
    TitleMessage.draw(firstWin)

    IntroMessage = Text(Point(360, 40), "A dice game")
    IntroMessage.setSize(20)
    IntroMessage.draw(firstWin)

    HighScores = Text(Point(290, 100), "High Scores:")
    HighScores.setSize(20)
    HighScores.draw(firstWin)
    
    playButton = Button(firstWin, Point(520, 50), 120, 60, "Let's Play!")
    exitButton = Button(firstWin, Point(70, 350), 100, 60, "Exit")
    playButton.activate()
    exitButton.activate()

    # Display High Scores
    x = 290
    y = 110
    infile = open('HighScores', 'r')
    for line in infile:
        name, score = line.split()
        y += 25
        msg = Text(Point(x, y), name + ": " + str(score))
        msg.setSize(12)
        msg.draw(firstWin)

    # User chooses to play or exit
    p = firstWin.getMouse()
    if exitButton.clicked(p):
        firstWin.close()
        return False
    elif playButton.clicked(p):
        firstWin.close()
        return True

def main ():
    x = splashScreen()
    if x:
# regular program
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()

if __name__=='__main__':
    main ()