# Stephen Stammen
# HW 4 - Part 1

import math as m
import random
import decimal



N = int(input('How many trials do you want to run of 100 coin tosses?     '))
def coinToss(N):
    sumTosses = 0
    exact50 = 0
    for i in range(N):
        tailCount = 0
        headCount = 0
        for x in range(100):
            coin = random.randint(1, 2)
            if coin == 1:
                headCount += 1
                sumTosses +=1
            elif coin == 2:
                tailCount += 1
                sumTosses += 1
        if headCount == 50:
            exact50 += 1
            print('We successful got 50 heads and 50 tails for the trial #', str(i+1))
    
    print('\nNumber of times we got 50 heads and tails =',exact50,'of',str(N),'trials.')
    ffChance = float(exact50/N) # times exactly 50 / total trials, ffChance = fifty fifty
    print('')
    print('Of', str(N), 'trials, there is a', "{:.001%}".format(ffChance),'chance of getting 50 heads')
    return ffChance, N

def main(N, ffChance):
    coinToss(N)
    ffMathTheory = ((m.factorial(100)) / (m.factorial(50)*m.factorial(50))) * m.pow(0.5, 100)
    tolerance = 0.00001
    while tolerance > abs(ffChance - ffMathTheory):
       N+=1
       coinToss(N)
main(N, ffChance)