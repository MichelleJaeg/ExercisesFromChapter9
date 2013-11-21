from random import randrange

def main (n):

    #Introduction
    print ("This program performs a simulation to estimate the probability of rolling ")
    print ("five-of-a-kind in a single roll of five six-sided dice.")

    #Simulation
    same = 0
    for i in range(n):
        die_1 = randrange(1, 7)
        die_2 = randrange(1, 7)
        die_3 = randrange(1, 7)
        die_4 = randrange(1, 7)
        die_5 = randrange(1, 7)
        if die_1 == die_2 and die_2 == die_3 and die_3 == die_4 and die_4 == die_5:
            same += 1
    probability = same/n

    #Print results
    print ("\nThe probability is", probability)



if __name__ == '__main__':
    main ()
