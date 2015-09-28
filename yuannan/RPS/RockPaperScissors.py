#/usr/bin/env python
#
# A "simple" rock paper scissors game
# Supports first to X
# Best out of X games
# Where X can be changed by the player
#
# Predefines
# debug = True
# Imports
import random
# Code starts here

def inputGamemode():
        global gamemode
        print("Which gamemode do you wish to play?")
        gamemodeBool=True
        while gamemodeBool:
                try:
                        gamemode=int(input("1) For first to X points\n2) Best out of X games\n"))
                        if gamemode in range(1,3):
                                gamemodeBool=False
                        else:
                                print("Gamemode is not within the acceptable options, only 1 or 2 please")
                except ValueError:
                        print("That is a valid integer!")

def inputRounds():
        global rounds
        if gamemode == 1:
                print("How many points do you need to get to win?")
        elif gamemode == 2:
                print("How many rounds do you wish to play until?")
        else:
                print("Programmers error, settings rounds to 3")
                rounds=3
        roundsBool=True
        while roundsBool:
                try:
                        rounds=int(input(""))
                        if rounds in range(1,11):
                                roundsBool=False
                        else:
                                print("Rounds is not within the acceptable options, only up to 10 please")
                except ValueError:
                        print("That is a valid integer!")

def compare(player,computer):
        if player == 1:
                if computer == 1:
                        return "Draw"
                elif computer == 2:
                        return False
                elif computer == 3:
                        return True
                else:
                        print("CRITICAL ERROR, compare player == 1")
                        return True # So program does not sepuku if I messed up somewhere
        elif player == 2:
                if computer == 1:
                        return True
                elif computer == 2:
                        return "Draw"
                elif computer == 3:
                        return False
                else:
                        print("CRITICAL ERROR, compare player == 2")
                        return True
        elif player == 3:
                if computer == 1:
                        return False
                elif computer == 2:
                        return True
                elif computer == 3:
                        return "Draw"
                else:
                        print("CRITICAL ERROR, compare player == 3")
                        return True
        else:
                print("CRITICAL ERROR!!! NO JK THIS TIME, COMPARE HAS FAILED")
                exit

def inputValues():
        global player
        playerValue = True
        # funky kode here, "True" is actully "False" or failed/retry and "False" is success/continue 
        while playerValue:
                try:
                        player=int(input("What would you want to play?\n1) Rock\n2) Paper\n3) Scissors\n"))
                        if player in range(1,4):
                                playerValue=False
                        else:
                                print("Value is not \"1-3\" (within the acceptable options)")
                                playerValue=True
                except:
                        print("Error, Value not a number/invalid!!!")
                        playerValue=True

def resultsGenerator():
        global results
        computer=random.randint(1,3)
        results=compare(player,computer)
        if "debug" in globals():
                print(computer)
                print(results,type(results))

def feedback():
        global computerPoints
        global playerPoints
        if results == True:
                print("Player Wins!")
                playerPoints+=1
        elif results == "Draw":
                print("It's a draw...")
        elif results == False:
                print("Computer wins!")
                computerPoints+=1
        else:
                print("Error in feedback, report to devs")

def again():
        print("Would you like to play again?")
        again=input("Y/n")
        if again.lower() == "y":
                print("Restarting game...")
        elif again.lower == "n":
                print("Goodbye!!!")
                game=False
                exit()
        else:
                print("That's not a valid option!, Y or N only please, not case sensitive.")

if __name__ == "__main__":
        print("Hello!\nWelcome to basic RPS!!!")
        game=True
        while  game:
                computerPoints,playerPoints=0,0
                inputGamemode()
                inputRounds()
                # Starts the diffrents game(modes)s here
                if gamemode == 1:
                        print("First to {} points!".format(rounds))
                        while computerPoints < rounds or playerPoints < rounds:
                                inputValues()
                                resultsGenerator()
                                print("") # breaks it up abit to make it abit more playable
                                feedback()
                        if computerPoints >= rounds:
                                print("The computer wins the game!!!\nBad luck, try again next time!")
                        elif playerPoints >= rounds:
                                print("You win!!! You have beaten a non-sentient being in a game based on purely chance!\nHow do you feel?")
                        else:
                                print("Error in gamemode 1")
                        
                elif gamemode == 2:
                        print("Best out of {} games!".format(rounds))
                        for i in range(rounds):
                                inputValues()
                                resultsGenerator()
                                print("")
                                feedback()
                        if playerPoints == computerPoints:
                                print("It's a draw!!! Better luck next time!")
                        else:
                                if playerPoints > computerPoints:
                                        print("You win!!! You have beaten a non-sentient being in a game based on purely chance!\nHow do you feel?")
                                elif computerPoints > playerPoints:
                                        print("You got rekt by the PC!!!Better luck next time.\nnoob.")
                                else:
                                        print("Error in gamemode2 endgame compare")
                
                else:
                        print("There is no gamemode {}!".format(gamemode))
                again()
