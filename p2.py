import random

board = ["-"] * 9
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("----------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("----------")
    print(board[6] + "|" + board[7] + "|" + board[8])

def playerInput(board):
    inp = int(input("Enter a number 1-9: ")) - 1
    if inp >= 0 and inp < 9 and board[inp] == "-":
        board[inp] = currentPlayer
    else:
        print("Oops player is already in that spot!")

def checkHorizontal(board):
    global winner
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] and board[i]!= "-":
            winner = board[i]
            return True
    return False

def checkRow(board):
    global winner
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i]!= "-":
            winner = board[i]
            return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!= "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2]!= "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()
            return

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)