# Stephen Stammen
#                           HW 1  -  SUM OF INTEGERS - PART 2
#import time module
from time import time

# obtain user input for the N integer to sum from 1 to N
print("Welcome to the sumation machine")
print("Choose the N integer to sum from 1 to N")
M = int(input('Enter the integer to stop at:  '))

# start the timer
tic = time()

#initialize acummulation
j = 0
newM = 0
#Loop until the M integer is reached
for i in range(1, M):
    looptic = time()
    newM = 0
    for j in range(10**i+1):
        newM += j
    if M>15:
        break #stop the program if M is too big
    looptoc = time()
    print('The iteration ', str(i),' took', str(looptoc - looptic), 'and added to: ', str(newM))
# end the timer
toc = time()

# print the time toc-tic
print('It took ', toc - tic, 'seconds to complete all the calculations')


