# Stephen Stammen
# HW 2 - Part 2
# Outputs were written at the bottom
import math as m

# Calculate the circumference of Earth
def calc_earth_circum(pi):
    r = 6370
    circ = 2 * pi * r
    print('Earths circumference is' ,  str(circ), 'km.')

# The Leibnitz Series - Using a while loop to check if its calculation of pi is within the actual value of pie.
def lsm_pi (M):
    tempPi = 0
    i = 0
    while 10**-(M+1) < abs(m.pi - tempPi*4): # While loop continues until the calculated pi is within the tolerence of M digits. TempPi *4 becasue equation only calcs pi
        denom = (2*i + 1)
        num = ((-1)**i)
        tempPi += num/denom
        i += 1
    print('Pi calculated to the', str(M), 'digit accurately')
    print(str(i) + ' terms used')
    pi = tempPi * 4 # Multiplied by 4 becasue tempPi = 1/4 pi
    calc_earth_circum(pi)
    return pi # higher M = more digits of pi

# The Nilankatha Series - Using a while loop to check if its calculation of pi is within the actual value of pie.
def nsm_pi(M):
    tempPi = 0
    i = 0
    while 10**-(M+1) < abs(m.pi - (tempPi + (3/4))*4): 
        denom = (((2*i+3)**3) - (2*i+3))
        num = ((-1)**i)
        nsmPI = (num/denom)
        tempPi += nsmPI
        i += 1
    print('Pi calculated to the', str(M), 'digit accurately')
    print(str(i) + ' terms used')
    pi = (3/4 + tempPi) * 4
    calc_earth_circum(pi)
    return pi


# The Adamchick Series - Using a while loop to check if its calculation of pi is within the actual value of pie.
def aw_pi(M):
    tempPi = 0
    i = 0
    while 10**-(M+1) < abs(m.pi - tempPi):
        acs = (4/(8*i+1) - (2/(8*i+4)) - (1/(8*i+5)) - (1/(8*i+6)))*((1/16)**i)
        tempPi += acs
        i += 1
    print('Pi calculated to the', str(M), 'digit accurately')
    print(str(i) + ' terms used')
    pi = tempPi
    calc_earth_circum(pi)
    return pi
    
# Choose a series - This allows the user to choose which series they want to run
def choose_series():
    series = str(input('''
--------------------------------------------------------------------------------------------------
Which series do you want to use?
            1) The Leibnitz Series
            2) The Nilankatha Series
            3) The Adamchick Series
Choose a number 1 to 3:  '''))
    print(' ' )
    M = int(input("Input an integer M:      "))
    if series == '1':
        print('\n                 THE LEIBNITZ SERIES')
        print('Pi is:     ', str(lsm_pi(M))) # These are converted to strings becasue as to not cause an error
        print()
    elif series == '2':
        print('\n                 THE NILANKATHA SERIES')
        print('Pi is:     ', str(nsm_pi(M)))
        print()
    elif series == '3':
        print('\n                 THE ADAMCHICK SERIES')
        print('Pi is:     ', str(aw_pi(M)))
        print()
    else:
        print('Was it that hard to pick a number between 1 and 3') # This is a joke


# The main function
def main():
    choose_again = 'yes'
    while choose_again.lower() == 'yes':
        choose_series()
        choose_again = str(input('Would you like to try another series equation?   yes / no   ')) #This allows the user to choose another series equation to try

# Call main function
main()

#OUTPUTS

#                  THE LEIBNITZ SERIES
# Pi calculated to the 3 digit accurately
# 10000 terms used
# Earths circumference is 40022.61640673704 km.
# Pi is:      3.1414926535900345


#                 THE NILANKATHA SERIES
# Pi calculated to the 6 digit accurately
# 135 terms used
# Earths circumference is 40023.89167282042 km.
# Pi is:      3.141592752968636


#                 THE ADAMCHICK SERIES
# Pi calculated to the 9 digit accurately
# 7 terms used
# Earths circumference is 40023.890406518505 km.
# Pi is:      3.141592653572881





