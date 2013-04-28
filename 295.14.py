#I wrote this slightly different than was asked in the problem statement, to allow
# for greater visibility of the walk


from random import random
from graphics import*
import math


def main ():

    #Introduction
    print ("This program traces a random walk in two dimensions. ")

    #Get input
    n=eval(input("\nHow many steps would you like the walker to take? "))

    #Create graphics window
    win=GraphWin("Random Walk",  400, 400)

   #Create random walk
    oldpoint=Point(200,200)
    oldpoint.draw(win)
    x=oldpoint.getX()
    y=oldpoint.getY()
    for i in range(n):
        angle=random() * 2 * math.pi
        x += 5 * math.cos(angle)
        y += 5 * math.sin (angle)
        newpoint=Point(x,y)
        newpoint.draw(win)
        line=Line(oldpoint,newpoint)
        line.draw(win)
        oldpoint=newpoint

    #Close window
    win.getMouse()
    win.close()



if __name__=='__main__':
    main ()