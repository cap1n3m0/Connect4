board = [
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],]

def printboard(board):
    for i in board:
        for l in i:
            print(l, end="")
        print("")


def checkWin(): 
    pass


printboard(board)

xPos = 0
yPos  = 0
win = False

while not win: 
    print("Player red, choose a position: ")
    xPos = int(input())
    yPos = int(input())
    board[xPos][yPos] = "r"
    if checkWin("r"):
        win = True
    print("Player yellow, choose a position: ")
    xPos = int(input())
    yPos = int(input())
    board[xPos][yPos] = "y"
    if checkWin("y"):
        win = True

