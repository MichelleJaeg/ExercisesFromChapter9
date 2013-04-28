from random import randrange

def main ():
    printIntro()
    n=getInput()
    bustnumber=simNGames(n)
    printSummary(n, bustnumber)

def printIntro():
    print ("This program simulates multiple games of blackjack to calculate ")
    print ("the probability that the dealer busts. ")

def getInput():
    n=eval(input("\nPlease enter the number of times that you would like to run the simulation. "))
    return n

def simNGames(n):
    #Simulates n games of blackjack from the perspective of the dealer
    busts=0
    for i in range(n):
        outcome=simOneGame()
        if outcome=="bust":
            busts+=1
    return busts

def simOneGame():
    #Simulates a single game of blackjack from the perspective of the dealer
    hand=0
    hasAce=False
    while hand<17:
        newcard=randrange(1,14)
        if newcard==1:
            hasAce=True
            hand+=1
        elif newcard==11 or newcard==12 or newcard==13:
            hand+=10
        else:
            hand+=newcard
        if hasAce:
            if 17<=hand+10<=21:
                hand+=10
    if hand>21:
        outcome="bust"
    else:
        outcome="notbust"
    return outcome

def printSummary(n,bustnumber):
    print ("\nGames simulated:", n)
    print ("Number of busts:", bustnumber)
    print ("Probability of busting is", bustnumber/n)

if __name__=='__main__':
    main()