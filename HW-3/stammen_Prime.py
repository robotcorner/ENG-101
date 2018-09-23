# Created by Stephen Stammen

# Creates an isPrime Function that works through the logic to see if the number is prime
def isPrime(num):
    if num > 1: # 1 is not prime
        for i in range(2, num): # checks all numbers between 2, and chosen number
            if num % i == 0: # for all those numbers, checks if it evenly divides by any number before it.
                return False #returns false if it is divisible by any number before it
        return True # returns True if its not divisible by any number before it.
    return False # returns false if num is not >1

    
def main():
    # Get a lower and upper integer from user entries
    lowerInt = int(input('Input lower range value start point for prime numbers:   '))
    upperInt = int(input('Input higher range value:   '))
    
    numPrime = 0 # start with 0 prime numbers
    numNonPrime = 1 # includes 1 because 1 is not checked
    myPrimeList = [] # this will keep track of all the prime numbers found, this could be exported as a csv
    
    for num in range(lowerInt+1, upperInt): # adds one to lowerint b/c python starts at 0
        if isPrime(num) == True:
            numPrime += 1 # if the isPrime fxn evaluates true, add 1 to count, and add it to the list
            myPrimeList.append(num)
        elif isPrime(num) == False: #if isPrime = False, add to nonPrime counter
            numNonPrime += 1
        else:
            print('Something Wrong Happened') # some error handling to tell the user to retry
    print('There are ', str(numPrime), 'prime numbers between', str(lowerInt), 'and',
    str(upperInt) + '.')
    print('There are ', str(numNonPrime), 'non-prime numbers between', str(lowerInt), 'and',
    str(upperInt) + '.')

main()

# There are  1636 prime numbers between 4,568 and 19,954.
# There are  13750 non-prime numbers between 4,568 and 19,954.
