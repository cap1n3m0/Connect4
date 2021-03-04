
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
        print("| ", end="")
        for l in i:
            print(l, end="")
            print(" | ", end="")
        print("")
        print("-----------------------------")


def placePiece(board, colour, col):
    if board[0][col] == "r" or board[0][col] == "y":
        print("This column is full")
        return False
    else:
        counter = 0
        for i in board:
            if i[col] == "r" or i[col] == "y":
                board[counter][col - 1] = colour
                print("print board")
                printboard(board)
                return True
        if board[5][col] == "o":
            print("printing board")
            
            board[5][col] = colour
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
