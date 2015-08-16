#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Simple battle ships game written in python
#
#By Yuannan Lin


import random
#debug=True
first_time=True
print("Welcome to battleships!")

def print_board(board):
    header="\|"
    neck="=|"
    for i in range(0,columns):
        number=i+1
        if i == 0:
            header=header+str(number)
            neck=neck+"="
        else:
            header=header+"-"+str(number)
            neck=neck+"=="
    print(header+"\n"+neck)
    number=1
    for row in board:
        print("{}|".format(number),end="")
        print("-".join(row))
        number+=1
    if 'debug' in globals():
        if debug:
            print(ship_col)
            print(ship_row)
        

def random_row(board):
    return random.randint(0, len(board)-1)

def random_col(board):
    return random.randint(0, len(board[0])-1)

def input_col():
    global guess_col
    guess_col_temp=int(input("Guess Col: "))
    if guess_col_temp > columns:
        print("Your number is too big, you only have",columns,"columns!")
        print("Please enter it agian!")
        input_col()
    elif guess_col_temp < 0:
        print("Your number is too small!")
        print("Please enter it agian!")
        input_col()
    else:
        guess_col=guess_col_temp
def input_row():
    global guess_row
    guess_row_temp=int(input("Guess Row: "))
    if guess_row_temp > rows:
        print("Your number is too big, you only have",rows,"rows!")
        print("Please enter it agian!")
        input_row()
    elif guess_row_temp < 0:
        print("Your number is too small!")
        print("Please enter it agian!")
        input_row()
    else:
        guess_row=guess_row_temp

def compare():
    global moves
    if guess_col-1 == ship_col and guess_row-1 == ship_row:
        moves+=1
        print("Congratulations! You sank my battleship in {} moves!\n".format(moves))
        agian=input("Do you want to play agian?\n")
        if agian.lower() == "yes" or agian.lower() == "y":
            global first_time
            first_time=True
            start_game()
        elif agian.lower() == "no" or agian.lower() == "n":
            print("Goodbye!")
            exit
    elif board[guess_row-1][guess_col-1] == "X":
        print("You already hit there!\nPlease try agian!")
        start_game()
    else:
        print("You missed my battleship!\n")
        moves+=1
        board[guess_row-1][guess_col-1] = "X"
        start_game()

def start_game():
    global columns
    global rows
    global ship_col
    global ship_row
    global first_time
    global moves
    if first_time:
        global board
        board=[]
        columns=int(input("How many columns do you want?\n"))
        rows=int(input("How many rows do you want?\n"))
        for x in range(0, rows):
            board.append(["O"] * columns)
        ship_col = random_col(board)
        ship_row = random_row(board)
        moves=0
        first_time=False
    print_board(board)
    input_col()
    input_row()
    compare()



start_game()

