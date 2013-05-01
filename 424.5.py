# Problem 5

# Find the rules to an interesting dice game and write an interactive program
# to play it. Some examples are Craps, Yachtzee, Greed, and Skunk.


from Prob5graphicsinterface import GraphicsInterface
from crapsApp import CrapsApp


def main ():

    inter = GraphicsInterface()
    app = CrapsApp(inter)
    app.run()

if __name__ == '__main__':
    main ()