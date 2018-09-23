# Stephen Stammen
# HW 4 - Part 2
# myCards.py

import random
def findFirstAce():
    shuffleDeck = random.sample(range(52),52) # Creates a list of 52 numbers/ cards that are randomly ordered
    ace0 = shuffleDeck.index(0) # finds ace1
    ace13 = shuffleDeck.index(13) # finds ace2
    ace26 = shuffleDeck.index(26) # finds ace3
    ace39 = shuffleDeck.index(39) #finds ace4

    aces = [] # creates a list of the positions where aces were just found in the shuffled deck
    aces.append(ace0) # These add the aces positions
    aces.append(ace13)
    aces.append(ace26)
    aces.append(ace39)
    aces.sort() # This organizes the aces by position

    firstAce = aces[0] # This gets the first position an ace was found at
    return firstAce

def main():
    allFirstAces = []
    trials = int(input('Input the number of trials you want to run:     ')) # Choose 1,000,000 trials
    i = 0
    while i < trials: # 1,000,000 Trials
        firstAce = findFirstAce()
        allFirstAces.append(firstAce)
        i += 1
    acePosTotal = sum(allFirstAces) # This is all the first aces positions added together
    print('The sum of all the first ace position is:  ', str(acePosTotal))
    acePosAvg = acePosTotal/(trials+1) # This divides the total ace positions by the number of trials to determine the average first ace postion
    print('The average first ace position is at approximately', str(round(acePosAvg, 3)))
main()

# Input the number of trials you want to run:     1000000
# The sum of all the first ace position is:   9587809
# The average first ace position is at approximately 9.588

# probability theory suggest the avg first position is 9.6 or 48/5