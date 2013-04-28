from random import random

def main ():
    #Introduction
    print ("This program estimates the value of pi according to the following idea: ")
    print ("Suppose you have a round dart board that just fits inside of a square cabinet.")
    print ("If you throw darts randomly, the proportion that hit the dart board vs. those ")
    print ("that hit the cabinet will be determined by the relative area of the dart board")
    print ("and the cabinet.")

    #Get input
    n=eval(input("\nPlease enter how many darts to throw. More darts=greater accuracy. "))

    #Simulation
    h=0
    for i in range(n):
        x=2*random()-1
        y=2*random()-1
        if x**2 + y**2<=1:
            h+=1
    pi=4*(h/n)

    #Print results
    print ("The simulation estimated the value of pi to be,", pi)





if __name__=='__main__':
    main ()