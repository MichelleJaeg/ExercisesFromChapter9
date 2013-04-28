from random import randrange

def main (n):

    #Introduction
    print ("This program performs a simulation to estimate the probability of rolling ")
    print ("five-of-a-kind in a single roll of five six-sided dice.")

    #Simulation
    same=0
    for i in range(n):
        die1=randrange(1,7)
        die2=randrange(1,7)
        die3=randrange(1,7)
        die4=randrange(1,7)
        die5=randrange(1,7)
        if die1==die2 and die2==die3 and die3==die4 and die4==die5:
            same+=1
    probability=same/n

    #Print results
    print ("\nThe probability is", probability)



if __name__=='__main__':
    main (100000)