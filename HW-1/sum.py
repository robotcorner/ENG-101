# Stephen Stammen
#HW 1  -  Part 2  -  Section 1
#                           SUM OF INTEGERS
#import time module
from time import time

# obtain user input for the N integer to sum from 1 to N
print("Welcome to the sumation machine")
print("Choose the N integer to sum from 1 to N")
N = int(input('Enter N:  '))

# start the timer
tic = time()

#initialize acummulation
j = 0
newN = 0

#Loop until the N-interger is reached
for j in range(1, N + 1):
    newN += j
    print(str(j),"            ", str(newN))
# end the timer
toc = time()

# print the time toc-tic
print('It took ', toc - tic, 'seconds to complete the calculations')

# N = 10,          55
# N = 30,         465
