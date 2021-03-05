from Player import Player
import Ai

playerRed = Player('r')
playerYellow = Player('y')
currentPlayer = playerRed

board = [
    ["o", "o", "o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o", "o", "o"], ]

#displays the board
def printboard(board):
    for i in board:
        print("| ", end="")
        for l in i:
            print(l, end="")
            print(" | ", end="")
        print("")
        print("-----------------------------")

#places the peice in whatever col they input
def placePiece(board, colour, col):
    col -= 1
    if not board[0][col] == "o":
        print("This column is full")
        return False
    else:
        counter = 0
        for i in board:
            if not i[col] == "o":
                print(counter)
                board[counter - 1][col] = colour
                printboard(board)
                
                return True
            counter += 1
        if board[5][col] == "o":
            board[5][col] = colour
            printboard(board)
    
#checks rows if someone won
def checkRows(board, color): 
    for i in board:
        currentStreak = 0
        for l in i:
            if l == color:
                currentStreak += 1
                if currentStreak == 4:
                    return True
            else:
                currentStreak = 0
    return False

#checks col if someone won
def checkColumns (board, color): 
    for i in range(7):
        currentStreak = 0
        for l in range(6):
            if board[l][i] == color:
                currentStreak += 1
            else: 
                currentStreak = 0
            
            if currentStreak == 4:
                return True
    
    return False

#checks diagonals if someone won
def checkDiagonals(board, color):
    for i in list(range(3)):
        for l in list(range(2)):
            if board[i][l] == color:
                if board[i + 1][l + 1] == color:
                    if board[i + 2][l + 2] == color:
                        if board[i + 3][l + 3] == color:

                            return True

    for i in list(range(3)):
        for l in list(range(2, 7)):
            if board[i][l] == color:
                if board[i + 1][l - 1] == color:
                    if board[i + 2][l - 2] == color:
                        if board[i + 3][l - 3] == color:
                            return True
    return False

#calls the other 3 winning functions (checkrow, checkcol, and checkDiagnol) and returns True if someone won
def hasWon(board, color):
    if checkRows(board, color) or checkColumns(board, color) or checkDiagonals(board, color):
        return True
    else:
        return False


xPos = 0
win = False

while not win:
    currentPlayer = playerRed
    print("Player red, choose a position: ")
    xPos = int(input())
    placePiece(board, currentPlayer.color, xPos)
    if not hasWon(board, 'r'):
        currentPlayer = playerYellow
        print("Player yellow, choose a position: ")
        xPos = int(input())
        placePiece(board, currentPlayer.color, xPos)
