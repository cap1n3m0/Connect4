class Player:
    color = 'r'
    win = False
    def __init__(self, c):
        self.color = c
        
    
playerRed = Player('r')

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

def placePiece(board, colour, col):
    if board[0][col] == "r" or board[0][col] == "y":
        print("This column is full")
        return board
    else:
        counter = 0
        for i in board:
            if i[col] == "r" or i[col] == "y":
                board[counter - 1][col] = colour
                return board
        board[-1][col] = colour

xPos = 0
yPos  = 0
win = False

while not win: 
    print("Choose a position: ")
    xPos = int(input())
    yPos = int(input())
    placePiece()
    print("Choose a position: ")
    xPos = int(input())
    yPos = int(input())
        placePiece()


