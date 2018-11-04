# Stephen Stammen
# HW 4 - Part 1

import math as m
import random
import decimal

def coinToss(N):
    sumTosses = 0
    exact50 = 0
    for i in range(N): # Choose Number of Trials
        tailCount = 0
        headCount = 0
        for x in range(100): # loop through 100 times
            coin = random.randint(1, 2) # chooses head or tails
            if coin == 1: # Counts if heads - I never actually used data though
                headCount += 1
                sumTosses +=1
            elif coin == 2: # Counts if tails - I never actually used this data though
                tailCount += 1
                sumTosses += 1
        if headCount == 50: # Counts if there are 50 heads and 50 tails
            exact50 += 1 
    return exact50
     # times exactly 50 / total trials, ffChance = fifty fifty
def main():
    # print('\nNumber of times we got 50 heads and tails =',exact50,'of',str(N),'trials.')
    N = 1
    ffMathTheory = ((m.factorial(100)) / (m.factorial(50)*m.factorial(50))) * m.pow(0.5, 100) # The theory provided in the HW
    tolerance = 0.001 # The tolerance specified, 
    exact50 = coinToss(N) # Had to run it first to get the while loop to work
    ffChance = float(exact50/N) # Calculates the chance of getting 50/50 heads out of N trials
    while tolerance < abs(ffChance - ffMathTheory): # Keeps looping until the probability is within the tolerance
        N+=1 # Increments the number of trials until the accuracy desired is achieved
        exact50 = coinToss(N)
        ffChance = float(exact50/N)
        
    print('The 50/50 probability theory calculates', str(ffMathTheory*100)) # times 100 for readability and like a %
    print('Calculated', str(ffChance*100)) # times 100 for readability and like a %
    print('It take', str(N), 'trials to calculate a', "{:.001%}".format(ffChance),'chance of getting 50 heads and 50 tails')
main()

# It took 75 trials to get within a tolerance of .001
# It took 566 trials to within a tolerance of .0001 
# It took 1621 trials  to get within a tolerance of .00001
