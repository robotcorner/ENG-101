# Stephen Stammen
#HW 2 - Part 1

#Calculate the circumference of Earth
def calc_earth_circum(pi):
    r = 6370
    circ = 2 * pi * r
    print('Earths circumference is' ,  str(circ), 'km.')

# The Leibnitz Series
def lsm_pi (n):
    tempPi = 0
    for i in range(0, n+1): #iterate through 10^i is passed in, when i = 1, the fuction goes through 10 times, 2 = 100, 3= 1000
        denom = (2*i + 1)
        num = ((-1)**i)
        tempPi += num/denom
    pi = tempPi * 4 # pi is multiplied by 4 because the equation only calculates pi/4
    calc_earth_circum(pi) # This calls the function that calculates the earths circumference using the pi just calculated
    return pi

# The Nilankatha Series
def nsm_pi(n):
    tempPi = 0
    for i in range(0, n+1):
        denom = (((2*i+3)**3) - (2*i+3))
        num = ((-1)**i)
        nsmPI = (num/denom)
        tempPi += nsmPI
    pi = (3/4 + tempPi) * 4 # in order to calc pi this equation added 3/4 and was then multiplied by 4 to = pi
    calc_earth_circum(pi)
    return pi

# The Adamchick Series
def aw_pi(n):
    tempPi = 0
    for i in range(0, n+1):
        acs = (4/(8*i+1) - (2/(8*i+4)) - (1/(8*i+5)) - (1/(8*i+6)))*((1/16)**i)
        tempPi += acs
    pi = tempPi #This equation calculated pi directly without the need to multiply the equation
    calc_earth_circum(pi)
    return pi
    
#Choose a series
def choose_series():
    series = str(input('''
-------------------------------------------------------------------
Which series do you want to use?
            1) The Leibnitz Series
            2) The Nilankatha Series
            3) The Adamchick Series
            4) Run All Series Equations
            
Choose a number 1 to 4:  '''))
    print(' ' )
    #Logic that determines which series you want to test
    if series == '1':
        print('                 Tests the Leibnitz Series')
        for i in range (1,4):
            print(str(10**i) + ' times through the loop =  '+ str(lsm_pi(10**i)))
            print()
    elif series == '2':
        print('                 Tests the Nilankatha Series')
        for i in range (1,4):
            print(str(10**i) + ' times through the loop =  ' + str(nsm_pi(10**i)))
            print()
    elif series == '3':
        print('                 Tests the Adamchick Series')
        for i in range (1,4):
            print(str(10**i) + ' times through the loop =  ' + str(aw_pi(10**i)))
            print()
    elif series == '4':
        print('                 Run All Series Equations\n\n')
        for i in range(1,4):
            print('                 Tests the Leibnitz Series')
            print(str(10**i) + ' times through the loop =  '+ str(lsm_pi(10**i)))
            print(" ")
            print('                Tests the Nilankatha Series')
            print(str(10**i) + ' times through the loop =  ' + str(nsm_pi(10**i)))
            print(" ")
            print('                 Tests the Adamchick Series')
            print(str(10**i) + ' times through the loop =  ' + str(aw_pi(10**i)))
            print(" ")
            print("-----------------------------------------------------------------")
    else:
        print('Was it that hard to pick a number between 1 and 3')


#The main function
def main():
    choose_again = 'yes'
    while choose_again.lower() == 'yes':
        choose_series()
        choose_again = str(input('\n Would you like to try another series equation?   yes / no   '))

#Call main function
main()

# Circumference of earth evaluated at 100 terms using each series:
        # Leibnitz Series:     40150.025929644 km
        # Nilakantha Series:     40023.893407670 km
        # Adamchick Series:     40023.890406733 km
