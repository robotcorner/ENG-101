import random # This is needed for the randint function
def startGame():
    #Telling the player what they can pick
    print("""
    1 = rock
    2 = lizard
    3 = spock
    4 = scissors
    5 = paper""" )

def gameMechanics():
    # playerChoice will remain a number while playerChoiceName will be the word describing the number for the user
    playerChoice = int(input("Enter a Number between 1 and 5     ")) # Player Chooses a Number based on what they see from startGame()
    choices = ['rock', 'lizard', 'spock', 'scissors', 'paper'] # List for choices to be named as words and not numbers when you win or lose
    playerChoiceName = choices[playerChoice-1] # assigns your chosen number a word but keeps the number intact for the game logic

    # opp will remain a number while oppName will be the word describing the number for the user
    opp = random.randint(1,5) # Chooses a Random Number between 1 and 5 for the opponent
    oppObjects = ['rock', 'lizard', 'spock', 'scissors', 'paper'] # List for choices to be named as words and not numbers when you win or lose
    oppName = oppObjects[opp-1] # assigns the computer's chosen number a word but keeps the number intact for the game logic
    
    print("\nYour Opponent:", str(opp), "   You:", str(playerChoice)) # This tells you whats going on to ensure the game is acting correctly and if the if else logic is faulty - This was great for debugging and can be removed for a final product
    print("Your Opponent:", str(oppName), "   You:", str(playerChoiceName),'\n') # This lets you see the words as an easy way to see if the if - else statements work correctly

    # You and the Computer choose the same thing
    if playerChoice == opp:
        print('It was a tie')
    
    # This logic is based off of the flowchart of the spockgame that was provided. I assigned each object a number
    # Player Chooses 1
    elif (playerChoice == 1 and (opp == 2 or opp == 4)): 
        print('Your', str(playerChoiceName), 'beat your opponents', str(oppName))
    elif (playerChoice == 1 and (opp == 3 or opp == 5)):
        print('Your', str(playerChoiceName), 'lost to your opponents', str(oppName))
    
    # Player Chooses 2
    elif (playerChoice == 2 and (opp == 3 or opp == 5)):
        print('Your', str(playerChoiceName), 'beat your opponents', str(oppName))
    elif (playerChoice == 2 and (opp == 1 or opp == 4)):
        print('Your', str(playerChoiceName), 'lost to your opponents', str(oppName))

    # Player Chooses 3
    elif (playerChoice == 3 and (opp == 4 or opp == 1)):
        print('Your', str(playerChoiceName), 'beat your opponents', str(oppName))
    elif (playerChoice == 3 and (opp == 2 or opp == 5)):
        print('Your', str(playerChoiceName), 'lost to your opponents', str(oppName))

    # Player Chooses 4
    elif (playerChoice == 4 and (opp == 2 or opp == 5)):
        print('Your', str(playerChoiceName), 'beat your opponents', str(oppName))
    elif (playerChoice == 4 and (opp == 1 or opp == 3)):
        print('Your', str(playerChoiceName), 'lost to your opponents', str(oppName))

    # Player Chooses 5
    elif (playerChoice == 5 and (opp == 1 or opp == 3)):
        print('Your', str(playerChoiceName), 'beat your opponents', str(oppName))
    elif (playerChoice == 5 and (opp == 2 or opp == 4)):
        print('Your', str(playerChoiceName), 'lost to your opponents', str(oppName))


def main():
    playAgain = 'yes' # Game starts first time
    while playAgain == 'yes': # will continue to run if playAgain is yes
        startGame() # lists the options
        gameMechanics() # runs the game
        playAgain = input("Would you like to play again? yes / no     ").lower()
        if playAgain == "yes" or playAgain == "y":
            playAgain = 'yes'
        else:
            playAgain = 'no'
main()