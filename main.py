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

printboard(board)

xPos = 0
yPos  = 0
print("Choose a position")
xPos = int(input())
yPos = int(input())

board[xPos][yPos] = "r"


