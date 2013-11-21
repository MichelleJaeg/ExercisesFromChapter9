from random import randrange

def main ():
    printIntro()
    n = getInput()
    bust_numbers = simNGames(n)
    printSummary(n, bust_numbers)

def printIntro():
    print ("This program simulates multiple games of blackjack to calculate ")
    print ("the probability that the dealer busts for each possible ")
    print ("starting value (card facing up initially). ")

def getInput():
    n = eval(input("\nPlease enter the number of times that you would like to run the simulation. "))
    return n

def simNGames(n):
    #Simulates n games of blackjack from the perspective of the dealer
    busts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        outcomes = simEachGame()
        for i in range(10):
            if outcomes[i] == "bust":
                busts[i] += 1
    return busts

def simEachGame():
    #Simulates a single game of blackjack from the perspective of the dealer
    #for each possible starting card
    outcomes = []
    for i in range(1, 11):
        hand = i
        if i == 1:
            hasAce = True
        else:
            hasAce = False
        while hand < 17:
            new_card = randrange(1, 14)
            if new_card == 1:
                hasAce = True
                hand += 1
            elif new_card == 11 or new_card == 12 or new_card == 13:
                hand += 10
            else:
                hand += new_card
            if hasAce:
                if 17 <= hand + 10 <= 21:
                    hand += 10
        if hand > 21:
            outcome = "bust"
        else:
            outcome = "notbust"
        outcomes.append(outcome)
    return outcomes

def printSummary(n,bust_numbers):
    print ("\nGames simulated:", n)
    for i in range(10):
        if i == 0:
            print ("\nStarting value: ace")
            print ("Number of busts:", bust_numbers[i])
            print ("Probability of busting is:", bust_numbers[i]/n)
        else:
            print ("\nStarting value:", i+1)
            print ("Number of busts:", bust_numbers[i])
            print ("Probability of busting is:", bust_numbers[i]/n)




if __name__ == '__main__':
    main()
