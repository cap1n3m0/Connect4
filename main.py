class Player:
    color = 'r'
    win = False

    def __init__(self, c):
        self.color = c


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


def printboard(board):
    for i in board:
        for l in i:
            print(l, end="")
        print("")

def placePiece(board, color, col):
    counter = 0
    for i in board:
        if i[col] == "o":
            board[counter - 1][col] = color
            return


def hasWon(board, color):
    #expected input (board, "r")
    #Rows
    for i in board:
        currentStreak = 0
        for l in i:
            if l == color:
                currentStreak += 1
                if currentStreak == 4:
                    return True
            else:
                currentStreak = 0
    
    #Columns
    for i in list(range(5)):
        currentStreak = 0
        for l in list(range(6)):

            if board[l][i] == color:
                currentStreak += 1
            else: 
                currentStreak = 0

            if currentStreak == 4:
                return True
    return False


xPos = 0
win = False

while not win:
    currentPlayer = playerRed
    print("Choose a position: ")
    xPos = int(input())
    placePiece(board, 'r', xPos)
    if not hasWon(board, 'r'):
        currentPlayer = playerYellow
        print("Choose a position: ")
        xPos = int(input())
        placePiece(board, 'y', xPos)
