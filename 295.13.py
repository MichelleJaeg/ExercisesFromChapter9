import random

def main (numtrials):


#Introduction
    print ("This program simulates a random walk,")
    print ("answering the question of how many steps away from the starting point one will")
    print ("end up if taking a random walk of n steps. ")

#Get input
    n=eval(input("\nHow many steps would you like to take? "))

#Simulation
    for i in range(numtrials):
        stepsaway=0
        x=0
        y=0
        for i in range(n):
            xstep=random.choice([-1,1])
            ystep=random.choice([-1,1])
            x+=xstep
            y+=ystep
        stepsaway+=abs(x-0) + abs(y-0)
    averagestepsaway=n//stepsaway

#Report results
    print ("\nThe average distance from the starting point was:", averagestepsaway, "steps.")



if __name__=='__main__':
    main (10000)


