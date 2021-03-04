
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
            print(l, end=" ")
        print("")


def placePiece(board, color, col):
    counter = 0
    for i in board:
        if i[col] == "o":
            board[counter - 1][col] = color
    print("printing board")
    printboard(board)
    
    

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
    for i in list(range(6)):
        currentStreak = 0
        for l in list(range(5)):
            if board[i][l] == color:
                currentStreak += 1
            else: 
                currentStreak = 0

            if currentStreak == 4:
                return True
     
    
    #Diagonals
    for i in list(range(3)):
        for l in list(range(2)):
            if board[i][l] == color:
                if board[i + 1][l + 1]:
                    if board[i + 2][l + 2]:
                        if board[i + 3][l + 3]:
                            return True

    for i in list(range(3)):
        for l in list(range(2, 7)):
            if board[i][l] == color:
                if board[i + 1][l - 1]:
                    if board[i + 2][l - 2]:
                        if board[i + 3][l - 3]:
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
