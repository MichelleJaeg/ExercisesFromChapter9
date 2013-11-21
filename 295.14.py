#This is written slightly differently than was asked in the problem statement, to allow
# for greater visibility of the walk

from random import random
from graphics import *
import math


def main ():

    #Introduction
    print ("This program traces a random walk in two dimensions. ")

    #Get input
    n = eval(input("\nHow many steps would you like the walker to take? "))

    #Create graphics window
    win = GraphWin("Random Walk",  400, 400)

   #Create random walk
    old_point = Point(200, 200)
    old_point.draw(win)
    x = old_point.getX()
    y = old_point.getY()
    for i in range(n):
        angle = random() * 2 * math.pi
        x += 5 * math.cos(angle)
        y += 5 * math.sin(angle)
        new_point = Point(x, y)
        new_point.draw(win)
        line = Line(old_point, new_point)
        line.draw(win)
        old_point = new_point

    #Close window
    win.getMouse()
    win.close()



if __name__ == '__main__':
    main ()
