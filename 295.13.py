import random

def main (numtrials):

#Introduction
    print ("This program simulates a random walk,")
    print ("answering the question of how many steps away from the starting point one will")
    print ("end up if taking a random walk of n steps. ")

#Get input
    n = eval(input("\nHow many steps would you like to take? "))

#Simulation
    for i in range(numtrials):
        steps_away = 0
        x = 0
        y = 0
        for i in range(n):
            x_step = random.choice([-1, 1])
            y_step = random.choice([-1, 1])
            x += x_step
            y += y_step
        steps_away += abs(x - 0) + abs(y - 0)
    average_steps_away = n // steps_away

#Report results
    print ("\nThe average distance from the starting point was:", average_steps_away, "steps.")



if __name__ == '__main__':
    main ()


