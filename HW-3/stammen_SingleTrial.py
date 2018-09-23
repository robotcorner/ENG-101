# Created by Stephen Stammen 9/14/18
from random import randint

myBirthday = randint(1,365) # random birthday chosen

randomBirthdaysM = [] # create a list for the random birthdays
sameDayProb = []

def main():
    print('You walk into a room of people. You want what the chance of someone \nhaving the same birthday as you is.')
    M = int(input('How many people are in the room?     ')) # M people
    nTrials = int(input('How many trials do you want to run?    ')) # Number of trials done
    for i in range(1, M+1): # add 1 because index starts at 0, 1 though number of people in the room
        nSuccess = 0 # Number of times someone has the same birthday as you.
        for j in range(nTrials):  # loops through every trial
            for k in range(i): # loops though each person
                if myBirthday == randint(1,365): #if random birthday = random persons birthday
                    nSuccess += 1 #add 1 to the count of people with the same birthday of all the trials.
                    break
        randomBirthdaysM.append(i)
        sameDayProb.append(nSuccess/nTrials)
    print('Of',str(nTrials) ,'trials,' ,str(nSuccess), ' rooms had a match')
    print('There is a',(nSuccess/nTrials)*100, '% chance of someone having the same birthday in each trial')

main()



