## İlker Rişvan
## 09/10/2020

import time
import random 
import sys


player = 'O' # player will use "O" letter in the game
ai = 'X'     # the macihine will use "X" letter in the game


# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# possible final positions for finish the game
winnerPositions = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])
finalPositons =([0,4,8],[2,4,6],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8])
# the game can be finish with these conditions
# examples are shown below for ai

# cross form
# _|_|X
# _|X|_
# X|_|_

# horizontal form
# _|_|_
# _|_|_
# X|X|X

# vertical form
# X|_|_
# X|_|_
# X|_|_


## Screen for game start and short brief ##
def gameStartScreen():
    print("\n")
    print("*** THE GAME IS STARTING GOOD LUCK *** \n")
    print("~~ YOUR LETTER IS 'O' AI'S 'X' ~~  \n")
    time.sleep(3) ## wait 3 sec

## information about board ##
def displayBoard():
    print("\n")
    print("     " + "  BOARD \n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "   " + "0 | 1 | 2")
    print(board[3] + " | " + board[4] + " | " + board[5] + "   " + "3 | 4 | 5")
    print(board[6] + " | " + board[7] + " | " + board[8] + "   " + "6 | 7 | 8")
    print("\n")

## pick the game starter ##
def isAiStartFirst():
    print("*** WHO WILL START ? SELECT MODE ***")
    print("(1) Start ")
    print("(2) Let start AI ")
    gameMode = int(input("(3) Random Start "))

    ## if player do not pick 1 or 2 or 3
    if gameMode < 1 or gameMode > 3:
        print("PLEASE PICK 1 OR 2 OR 3 \n ")
        time.sleep(3)
        isAiStartFirst() ## for pick again
    ## starter is player
    if gameMode == 1:
        print("\n")
        print("*** YOU ARE STARTING *** \n")
        print("BOARD LIKE AS SHOWN IN BELOW")
        print("0 | 1 | 2")
        print("3 | 4 | 5")
        print("6 | 7 | 8")
        return False
    ## starter is machine
    if gameMode == 2:
        print("\n")
        print("*** AI IS STARTING NOW *** \n")
        return True
    ## starter will be random
    if gameMode == 3:
        print("*** Wait a 2 sec. I will decide. *** \n")
        time.sleep(2)
        whoIsFirst = random.choice([True, False]) # for pick starter randomly

        if whoIsFirst: # ai will start
            print("\n")
            print("*** AI IS STARTING ***")
            return True
        if not whoIsFirst: # player will start
            print("\n")
            print("*** BE READY AGAINST AI YOU ARE STARTING ***")
            return False

## method for player's moves ##
def Player():
    playerPosition =  input("Pick a number from 0-8 now. \n") #input from player

    #if chosen piece free move there
    if board[int(playerPosition)] == "-":
        board[int(playerPosition)] = "O"
    else: # if not pick again
        print("UPS! Pick another number!")
        Player()

    print("Your move is below. \n")
    displayBoard() #show player move

## method for count machine's moves ##
def aiMoveCounter():
    aiCounter = 1 # this counter important because we control is machine play first or second
                  # started with 1 because ai will 1 move in the begging its certain and we will use
                  # this method after this move

    for i in range(len(board)): # if there is X on board counter ++
        if board[i] == "X":
            aiCounter +=1
    return  aiCounter

## method for count player's moves ##
def playerMoveCounter():
    playerCounter = 0
    for i in range(len(board)): # how many 'O' letters is exist on the board
        if board[i] == "0":     # and count them
            playerCounter +=1   # count with ++
    return  playerCounter

## draw screen ##
def Draw():
    print("***FINAL SHAPE OF BOARD ***")
    displayBoard()
    print("************************** \n")
    print("          DRAW             \n")
    print("************************** \n")
    sys.exit(0)

## the machine's moves ##
def AI():
    aiCounter = aiMoveCounter()
    playerCounter = playerMoveCounter()

    isAiMoved = False
#in this method machine try to win firstly if its not possible check to
# #player's possibility of  win and stop the player
#we need to divide the board into 3 parts as corners,sides and center
#if player did not pick center or machine start the game, machine kept the center.as shown in below
#and then machine will kept corners if these pieces are free
#in the end machine will kept

    corners = [0, 2, 6, 8]
    sides = [1, 3, 5, 7]

    # center position select center if its free
    if playerCounter == 0 and board[4] == "-":
        board[4] = ai
        isAiMoved =True

    # check for is win is possible
    if aiCounter > 2 and not isAiMoved:
        checkWinPossible()


    # stop the player
    for stopPlayer in finalPositons:
        if board[stopPlayer[0]] == "O" and board[stopPlayer[1]] == "O" and board[stopPlayer[2]] != "X":
            board[stopPlayer[2]] = "X"
            isAiMoved = True
            break
        if board[stopPlayer[0]] == "O" and board[stopPlayer[2]] == "O" and board[stopPlayer[1]] != "X":
            board[stopPlayer[1]] = "X"
            isAiMoved = True
            break
        if board[stopPlayer[1]] == "O" and board[stopPlayer[2]] == "O" and board[stopPlayer[0]] != "X":
            board[stopPlayer[0]] = "X"
            isAiMoved = True

    # pick a corner if there is no change to win or lose
    if not isAiMoved:
        for i in corners:
            if board[i] == "-":
                cornerMove = random.choice(corners)
                if board[cornerMove] == "-":
                    board[cornerMove] = ai
                    isAiMoved = True
                    break
    # pick a side if there is no change to win or lose
    if not isAiMoved:
        for i in sides:
            if board[i] == "-":
                sideMove = random.choice(sides)
                if board[sideMove] == "-":
                    board[sideMove] = ai
                    isAiMoved = True
                    break

    if not isAiMoved:
        for i in range(len(board)):
            if board[i] == "-":
                board[i] == ai
                isAiMoved = True
                break
            if board[i] != "-":
                Draw()


    print("AI's move is below. \n")
    displayBoard()



## finish the game if its possible and go finish screen
def checkWinPossible():
    for finalMove in finalPositons:
        if board[finalMove[0]] == "X" and board[finalMove[1]] == "X" and board[finalMove[2]] != "O":
            board[finalMove[2]] = "X"
            endOfGame() # if code access here the game ends automatically
            break
        if board[finalMove[1]] == "X" and board[finalMove[2]] == "X" and board[finalMove[0]] != "O":
            board[finalMove[0]] = "X"
            endOfGame()
            break
        if board[finalMove[0]] == "X" and board[finalMove[2]] == "X" and board[finalMove[1]] != "O":
            board[finalMove[1]] = "X"
            endOfGame()
            break

#finish screen
def endOfGame():
    print("***FINAL SHAPE OF BOARD ***")
    displayBoard()
    print("************************** \n")
    print("AI WON, I AM SORRY FOR YOU. \n")
    print("************************** \n")
    sys.exit(0)

#main method for game
def Game():

   gameStartScreen()
   starter = isAiStartFirst()
   while True:
       if not starter: # if starter is player
                Player()
                AI()
       if starter: # if starter is machine
               AI()
               Player()

Game()



