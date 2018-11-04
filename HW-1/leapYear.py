#Leap Year HW 1 - Part 1
#Created by Stephen Stammen

#This program takes in a range of dates and outputs the number of leap years in between

#Get input on the range of years
year1 = int(input('Enter the start year:  '))
year2 = int(input('Enter the end year:  '))


myCount = 0 #initialize counter

for year in range(year1, year2 + 1): #for loop to count the number of years between the first and the last year
    if year % 4 == 0 : #Evenly divisible by 4
            if year % 100 != 0: #not evenly divisible by 100 = leap year
                myCount += 1 #add 1 to the count of leapYears between the range
                #print(year, ':  LEAP YEAR')            
            elif year % 100 == 0: #Evenly divisible by 100
                if year % 400 == 0: #year evenly divisible by 400; add as leap year
                    myCount += 1 
                    #print(year, ':  LEAP YEAR') 
                #elif year % 400 != 0: #year not evenly divisble by 400 = not leap year
                    #print(year, ':  NOT LEAP YEAR')  
    #elif year %4 != 0: #Not evenly divisible by 4
        #print(year, ':  NOT LEAP YEAR')


print('There are ', str(myCount), 'leap years between ', str(year1), 'and', str(year2)) #print the number of years between the range



#Leap years between 1600, 3200:    389







