# Created by Stephen Stammen

# Create an isPrime Function
def isPrime(num):
    '''Returns True if n is prime'''
    if num > 1: # 1 is not prime
        for i in range(2, num): # This excludes 1 when looping
            if num % i == 0: #
                print('Im returning false')
                return False
        print('Im returning true')
        return True
    print('Im returning false')
    return False
    #Trying to understand the logic above

    
def main():
    # Get a lower and upper integer from user entries
    lowerInt = int(input('Input lower range value start point for prime numbers:   '))
    upperInt = int(input('Input higher range value:   '))
    
    numPrime = 0
    numNonPrime = 1 # includes 1 because 1 is not checked
    myPrimeList = []
    
    for num in range(lowerInt+1, upperInt):
        if isPrime(num) == True: # or == 1?
            numPrime += 1
            myPrimeList.append(num)
        elif isPrime(num) == False:
            numNonPrime += 1
        else:
            print('Something Wrong Happened')
    print('There are ', str(numPrime), 'prime numbers between', str(lowerInt), 'and',
    str(upperInt) + '.')
    print('There are ', str(numNonPrime), 'non-prime numbers between', str(lowerInt), 'and',
    str(upperInt) + '.')
    if upperInt < 200:
        print('Prime list', myPrimeList)

main()

# There are  1636 prime numbers between 4,568 and 19,954.
# There are  13750 non-prime numbers between 4,568 and 19,954.
