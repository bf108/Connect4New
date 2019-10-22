#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 09:31:20 2019

@author: benfarrell
"""
''' ----------------Functions------------------------'''
#Function which counts up Colums, Rows, Diagonals
def check_winner(board, p1, p2, win_crit):
    import re  
    #Define search pattern
    pat1 = re.compile("X{%d}" % (win_crit))
    pat2 = re.compile("O{%d}" % (win_crit))
    
    #check rows for 4 in a row X or O
    for i in range(len(board)):
        row = "".join(board[i])
        if bool(re.search(pat1,row)):
            return("%s Wins" % p1)
        elif bool(re.search(pat2,row)):
            return("%s Wins" % p2)
    
    #check cols for 4 in a row X or O
    for i in range(len(board[0])):
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        col_t = "".join(col)
        if bool(re.search(pat1,col_t)):
            return("%s Wins" % p1)
        elif bool(re.search(pat2,col_t)):
            return("%s Wins" % p2)
            
    # Diagonals R to L    
    for i in range((len(board[0])*2-2),-1,-1):
        diag = []
        for j in range(len(board)):
            if i-j >= 0:
                try:
                    diag.append(board[j][i-j])
                except:
                    ""
            diag_t = "".join(diag)
            if bool(re.search(pat1,diag_t)) == True:
                return("%s Wins" % p1)
                
            elif bool(re.search(pat2,diag_t)) == True:
                return("%s Wins" % p2)
    
    #Cover Diagonals L to R
    for i in range(-(len(board[0])-1),len(board),1):
        diag = []
        for j in range(len(board)):
            if i+j >= 0:
                try:
                    diag.append(board[j][i+j])
                except:
                    ""
        
        diag_t = "".join(diag)
        if bool(re.search(pat1,diag_t)) == True:
            return("%s Wins" % p1)
            
        elif bool(re.search(pat2,diag_t)) == True:
            return("%s Wins" % p2)
        
        
    return("No Winner")

#Functin to check whether board is full
def check_full(board):
    for row in board:
        if "-" in row:
            return ("No")
    return ("Full")

#Function to Allow Disc to Be Inserted and Board Updated
def Insert_Token(board, go, col):
    for i in range(len(board)-1,-1,-1):
        if board[i][col-1] == "-":
            board[i][col-1] = go
            return (board)

'''-------------------------- Game ---------------------------------'''
#Welcome to the game
print ("Welcome to Connect Four!")
#Enter player details
p1, p2 = input("Please enter Player 1 name: "), input("Please enter Player 2 name: ")

#Define Grid Size
rows, columns = int(input("Input Number of Rows: ")), int(input("Input Number of Columnss: "))

#Define Win Criteria
win_crit = int(input("Input Num of Sequential Tokens Required to Win: "))

#Set up variable for game loop
play = "Yes"
#Players total scores
p1t = 0
p2t = 0

while play == "Yes":
    #Reset Play to empyt
    play = ""
    # Counter for repeat goes when incorrect value or full col selected
    count = 0
    #create board
    board = []
    for i in range(rows):
        board.append(["-"]*columns)
    #Print Board
    [print(" ".join(item),end="\n") for item in board]
    
    #Loop thru game if there are no winners and board isn't full
    while check_winner(board,p1,p2,win_crit) == "No Winner" and check_full(board) == "No":
        #Col variable used as player selection of where to go - Set to -1 initially
        col = -1
        #Player 1 Go
        if count % 2 == 0:
            repeat = 0
            #Ensures that col selected by player is within limits and not full
            while col < 0 or col > len(board[0]) or board[0][col-1] != "-":
                if repeat == 0:
                    print("\n","%s's Go" %(p1),"\n")
                    col = int(input("Pick a column between %d and %d: " %(0,len(board))))
                    repeat += 1
                else:
                    print("\n","Still %s's Go" %(p1),"\n")
                    col = int(input("Ensure Column isn't FULL and is within range %d and %d: " %(0,len(board))))
                    repeat += 1
            #Board Updated       
            board = Insert_Token(board,"X",col)
        #Player 2 Go    
        else:
            repeat = 0
            while col < 0 or col > len(board[0]) or board[0][col-1] != "-":
                if repeat == 0:
                    print("\n","%s's Go" %(p2),"\n")
                    col = int(input("Pick a column between %d and %d: " %(0,len(board))))
                    repeat += 1
                else:
                    print("\n","Still %s's Go" %(p2),"\n")
                    col = int(input("Ensure Column isn't FULL and is within range %d and %d: " %(0,len(board))))
                    repeat += 1
                    
            board = Insert_Token(board,"O",col)
        #Prints updated Board    
        print("\n","Updated Baord","\n")
        [print(" ".join(item),end="\n") for item in board]
        #Updates count to change player go
        count += 1
    #Prints Winner once out of game loop
    print("\n",check_winner(board,p1,p2,win_crit),"\n")
    #Adds up total scores
    if check_winner(board,p1,p2,win_crit) == "%s Wins" %(p1):
        p1t += 1
    elif check_winner(board,p1,p2,win_crit) == "%s Wins" %(p2):
        p2t += 1
        
    print("Overall Scores","\n","%s: %d" %(p1,p1t),"\n","%s: %d" %(p2,p2t))
    #Asks if players would like to go again?
    while play != "Yes" and play != "No":
        play = input("Would you like to play agian?: Input Yes or No  ")
    
print ("End of Game")
           
        