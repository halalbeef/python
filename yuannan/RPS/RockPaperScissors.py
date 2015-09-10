#/usr/bin/env python
#
# A "simple" rock paper scissors game
# Supports best to X
# Best out out of X games
# Where X can be changed by the player

import random

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

print("Hello!\nWelcome to basic RPS!!!")
computer=random.randint(1,3)
print(computer)
inputValues()
results=compare(player,computer)
print(results,type(results))
if results == True:
        print("Player Wins!!!")
elif results == "Draw":
        print("It's a draw!!!")
elif results == False:
        print("Computer wins...")
else:
        print("Error in compare!!!")
