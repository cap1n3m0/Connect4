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
    if board[0][col] == "r" or board[0][col] == "y":
        print("This column is full")
        return False
    else:
        counter = 0
        for i in board:
            if i[col] == "r" or i[col] == "y":
                board[counter - 1][col] = color
                return True
        board[-1][col] = color


def hasWon(board, color):
    # expected input (board, "r")
    # columns
    global currentPlayer
    for i in board:
        currentStreak = 0
        for l in i:
            if l == color:
                if currentPlayer.color == color:
                    currentPlayer.color += 1
                    if currentPlayer.color == 4:
                        return True
            else:
                pass


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
