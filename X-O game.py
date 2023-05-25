# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from IPython.display import clear_output

def printboard(board):
    clear_output()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def editboard(num,ch,board):
    x=""
    if ch.upper()=="X":
        x="X"
    elif ch.upper()=="O":
        x="O"
    else:
        x="enter the X or O"
    if num==1 and board[6]!="X" and board[6]!="O":
        board[6]=x
    elif num==2 and board[7]!="X" and board[7]!="O":
        board[7]=x
    elif num==3 and board[8]!="X" and board[8]!="O":
        board[8]=x
    elif num==4 and board[3]!="X" and board[3]!="O":
        board[3]=x
    elif num==5 and board[4]!="X" and board[4]!="O":
        board[4]=x
    elif num==6 and board[5]!="X" and board[5]!="O":
        board[5]=x
    elif num==7 and board[0]!="X" and board[0]!="O":
        board[0]=x
    elif num==8 and board[1]!="X" and board[1]!="O":
        board[1]=x
    elif num==9 and board[2]!="X" and board[2]!="O":
        board[2]=x
    else:
        editboard(int(input("Enter A Number from (1-9) and that is not taken already ")), ch, board)
    return board
def checkthestateoftheboard(board):
    state=""
    if board[0]==board[1]==board[2]=="X" or board[0]==board[1]==board[2]=="O":
        state="Win"
    elif board[0]==board[3]==board[6]=="X" or board[0]==board[3]==board[6]=="O":
        state="Win"
    elif board[0]==board[4]==board[8]=="X" or board[0]==board[4]==board[8]=="O":
        state="Win"
    elif board[2]==board[5]==board[8]=="X" or board[2]==board[5]==board[8]=="O":
        state="Win"
    elif board[2]==board[4]==board[6]=="X" or board[2]==board[4]==board[6]=="O":
        state="Win"
    elif board[6]==board[7]==board[8]=="X" or board[6]==board[7]==board[8]=="O":
        state="Win"
    elif board[3]==board[4]==board[5]=="X" or board[3]==board[4]==board[5]=="O":
        state="Win"
    elif board[1]==board[4]==board[7]=="X" or board[1]==board[4]==board[7]=="O":
        state="Win"
    elif (board[0]=="X" or board[0]=="O") and (board[1]=="X" or board[1]=="O") and (board[2]=="X" or board[2]=="O") and (board[3]=="X" or board[3]=="O") and (board[4]=="X" or board[4]=="O") and (board[5]=="X" or board[5]=="O") and (board[6]=="X" or board[6]=="O") and (board[7]=="X" or board[7]=="O") and (board[8]=="X" or board[8]=="O"):
        state="Draw"
    else:
        state="Still Going"
    return state

def printstate(state):
    if state=="Win":
        print("Congratulations u won the game Do u want to play again?")
        c=input("Enter Yes or No").upper()
        while c!="YES" and c!="NO":
            print("Please enter the Yes or No")
            c=input("Enter Yes or No ").upper()
        if c == "YES":
            replay()
        else:
            print("Thanks for Playing")
    elif state=="Draw":
        print("Its a Draw ")
        print("Do u want to play again ")
        c=input("Enter Yes or No ").upper()
        while c!="YES" and c!="No":
            print("Please enter the Yes or No")
            c=input("Enter Yes or No").upper()
        if c == "YES":
            replay()
        else:
            print("Thanks for Playing")

def replay():
    game()
    pass

def player1input (ch):
    x=""
    if ch.upper()=="X":
        x="X"
    elif ch.upper()=="O":
        x="O"
    else:
        x="enter the X or O"
    return x

def game():
    board=[" "," "," "," "," "," "," "," "," "]
    print("Welcome to Tic Tac Toe!")
    player1=player1input(input("Player 1:Do you want to be X or O?\n"))
    if player1.upper()=="X":
        player2input="O"
    else:
        player2input="X"
        print("Player 1 will go First.")
   
    c=input("Are u Ready to play Yes or No ").upper()
    while c!="YES" and c!="No":   
        print("Please enter the Yes or No")
        c=input().upper()
    if c == "YES":
        while checkthestateoftheboard(board)=="Still Going":
            clear_output(wait=False)
            clear_output(wait=False)
            clear_output(wait=False)
            printboard(board)
            print("----------------------")
            print("Player 1: ")
            printboard(editboard(int(input("Choose Your next position: (1-9) ")), player1,board))
            clear_output(wait=True)
            if checkthestateoftheboard(board)=="Still Going":
                print("Player 2: ")
                editboard(int(input("Choose Your next position: (1-9) ")), player2input,board)
            printstate(checkthestateoftheboard(board))
       
        else:
            print("Thanks for Playing")
game()










