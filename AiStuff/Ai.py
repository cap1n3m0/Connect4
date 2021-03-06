import random

# Did they tie?
def didTie(board):
    for i in board[0]:
        if i == "o":
            return False
    return True
    
#checks rows if someone won
def checkRows(board, color): 
    for row in board:
        currentStreak = 0
        for col in row:
            if col == color:
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
    # print(checkRows(board, color))
    # print(checkColumns(board, color))
    # print(checkDiagonals(board, color))
    if checkRows(board, color) or checkColumns(board, color) or checkDiagonals(board, color):
        #print("ygckvbukgvbkuyghvkuyghvkyugvk")
        return True
    else:
        return False

#places the peice in whatever col they input
def placePiece(board, colour, col):
    col -= 1
    if board[0][col] == "o":
        counter = 0
        for i in board:
            if not i[col] == "o":
                board[counter - 1][col] = colour
                return True
            counter += 1

        if board[5][col] == "o":
            board[5][col] = colour

    else:
        return False

# check to see if it is a vaild location to put things
def vaildLocation(board, col):
    col -= 1
    if board[0][col] == "o":
        counter = 0
        for i in board:
            if i[col] == "o":
                return True
            counter += 1
    else:
        return False
            
# Check for all of the 3 pairs of a color
def checkThree(board, piece):
    three_count = 0
    rowAmount = len(board)
    colAmount = len(board[0])
    emptyspaceChar = Ai.emptyspaceChar

    for r in range(rowAmount-1):
        for c in range(colAmount-1):
            if c < colAmount-3:
                # check horizontal right
                if board[r][c] == board[r][c+1] == board[r][c+2] == piece and board[r][c+3] == emptyspaceChar:
                    three_count += 1
                
                if r < rowAmount-3:
                    # check diagnoal right
                    if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == piece and board[r+3][c+3] == emptyspaceChar:
                        three_count += 1
            
            if c >= 3:
                # check horizontal left
                if board[r][c] == board[r][c-1] == board[r][c-2] == piece and board[r][c-3] == emptyspaceChar:
                    three_count += 1
                
                if r < rowAmount-3:
                    # check diagnoal left
                    if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == piece and board[r+3][c-3] == emptyspaceChar:
                        three_count += 1
            
            if r < rowAmount-3:
                # chek vertical
                if (board[r][c] == board[r+1][c] == board[r+2][c] == piece and board[r+3][c] == emptyspaceChar) or (board[r+1][c] == board[r+2][c] == board[r+3][c] == piece and board[r][c] == emptyspaceChar):
                    three_count += 1
    
    return three_count

# Check for all of the 2 pairs of a color
def checkTwo(board, piece):
    twoCount = 0
    rowAmount = len(board)
    colAmount = len(board[0])
    emptyspaceChar = Ai.emptyspaceChar

    for r in range(rowAmount-1):
        for c in range(colAmount-1):
            if c < colAmount-3:
                # check horizontal right
                if board[r][c] == board[r][c+1] == piece and board[r][c+2] == board[r][c+3] == emptyspaceChar:
                    twoCount += 1
                
                if r < rowAmount-3:
                    # check diagnoal right
                    if board[r][c] == board[r+1][c+1] == piece and board[r+2][c+2] == board[r+3][c+3] == emptyspaceChar:
                        twoCount += 1
            
            if c >= 3:
                # check horizontal left
                if board[r][c] == board[r][c-1] == piece and board[r][c-2] == board[r][c-3] == emptyspaceChar:
                    twoCount += 1
                
                if r < rowAmount-3:
                    # check diagnoal left
                    if board[r][c] == board[r+1][c-1] == piece and board[r+2][c-2] == board[r+3][c-3] == emptyspaceChar:
                        twoCount += 1
            
            if r < rowAmount-3:
                # chek vertical
                if (board[r][c] == board[r+1][c] == piece and board[r+2][c] == board[r+3][c] == emptyspaceChar) or (board[r+2][c] == board[r+3][c] == piece and board[r][c] == board[r+1][c] == emptyspaceChar):
                    twoCount += 1

    return twoCount

# Pick the best move to take
def pickBestMove(board, piece, AIpiece, PLAYERpiece):
    playableLocations = findPlayableLocations(board)
    bestScore = float("-inf")
    bestCol = random.choice(playableLocations)

    for col in playableLocations:
        temp_board = board
        placePiece(temp_board, piece, col)

        if hasWon(temp_board, AIpiece):
            score = Ai.returnValue
        else:
            score = calculate_score(board, AIpiece, PLAYERpiece)

        if score > bestScore:
            bestScore = score
            bestCol = col
    
    return bestCol

# Find all playable colums
def findPlayableLocations(board):
    playableLocations = []
    colAmount = len(board[0])

    for col in range(colAmount-1):
        if vaildLocation(board, col+1):
            playableLocations.append(col+1)
    
    return playableLocations

# Calculate a score
def calculate_score(board, AIpiece, PLAYERpiece):
    threeScore = checkThree(board, AIpiece)*4
    twoScore = checkTwo(board, AIpiece)*2
    AiWon = hasWon(board, AIpiece)

    playerThreeScore = checkThree(board, PLAYERpiece)*8
    playerTwoScore = checkTwo(board, PLAYERpiece)*4
    playerWon = hasWon(board, PLAYERpiece)

    score = (threeScore + twoScore + 1000 if AiWon else 0) - (playerThreeScore + playerTwoScore + 1000 if playerWon else 0)

    return score

def enemyCanWin(board, PLAYERpiece):
    three_score = checkThree(board, PLAYERpiece)
    if three_score > 0:
        rowAmount = len(board)
        colAmount = len(board[0])
        emptyspaceChar = Ai.emptyspaceChar

        for r in range(rowAmount-1):
            for c in range(colAmount-1):
                if c < colAmount-3:
                    # check horizontal right
                    if board[r][c] == board[r][c+1] == board[r][c+2] == PLAYERpiece and board[r][c+3] == emptyspaceChar:
                        return c + 3
                    
                    if r < rowAmount-3:
                        # check diagnoal right
                        if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == PLAYERpiece and board[r+3][c+3] == emptyspaceChar:
                            return c + 3
                
                if c >= 3:
                    # check horizontal left
                    if board[r][c] == board[r][c-1] == board[r][c-2] == PLAYERpiece and board[r][c-3] == emptyspaceChar:
                        return c - 3
                    
                    if r < rowAmount-3:
                        # check diagnoal left
                        if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == PLAYERpiece and board[r+3][c-3] == emptyspaceChar:
                            return c - 3
                
                if r < rowAmount-3:
                    # chek vertical
                    if (board[r][c] == board[r+1][c] == board[r+2][c] == PLAYERpiece and board[r+3][c] == emptyspaceChar) or (board[r+1][c] == board[r+2][c] == board[r+3][c] == PLAYERpiece and board[r][c] == emptyspaceChar):
                        return c

    else:
        return None

class Ai:

    returnValue = 1000000000000
    emptyspaceChar = "o"

    def __init__(self, aiColor="r", playerColor="y"):
        self.color = aiColor
        self.aiColor = aiColor
        self.playerColor = playerColor
        self.Pinfinity = float("inf")
        self.Ninfinity = float("-inf")
        self.lastCol = None
        self.start = True
    
    def makeBoardCopy(self, board):
        temp_board = []
        for row in board:
            temp = []
            for column in row:
                temp.append(column)
            temp_board.append(temp)
        
        return temp_board


    def minMax(self, board, depth, alpha, beta, maximizingPlayer):
        if self.start is True:
            self.lastCol = None
        self.start = False
        playableLocations = findPlayableLocations(board)
        hasWonAi = hasWon(board, self.aiColor)
        hasWonPlayer = hasWon(board, self.playerColor)
        isTie = didTie(board)

        terminal = True if hasWonAi or hasWonPlayer or isTie else False

        if depth == 0 or terminal:
            if terminal:
                if hasWonAi:
                    return (self.lastCol, float("inf"))

                elif hasWonPlayer:
                    return (self.lastCol, float("-inf"))
                
                else:
                    return (self.lastCol, 0)

            else:
                return (self.lastCol, calculate_score(board, self.aiColor, self.playerColor))
        
        # Ai's turn
        if maximizingPlayer:
            value = self.Ninfinity
            
            column = random.choice(playableLocations)
            for col in playableLocations:
                temp_board = self.makeBoardCopy(board)
                placePiece(temp_board, self.aiColor, col)

                newScore = self.minMax(temp_board, depth-1, alpha, beta, False)[1]

                if newScore > value:
                    value = newScore
                    column = col
                    self.lastCol = column

                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return (column, value)

        # Player's turn
        else:
            value = self.Pinfinity
            column = random.choice(playableLocations)
            for col in playableLocations:
                temp_board = self.makeBoardCopy(board)
                placePiece(temp_board, self.playerColor, col)
                playerWon = hasWon(temp_board, self.playerColor)

                newScore = self.minMax(temp_board, depth-1, alpha, beta, True)[1]

                if newScore < value:
                    value = newScore
                    column = col
                    self.lastCol = column
                
                # if playerWon:
                #     value = float("inf")
                #     print(beta)

                alpha = min(alpha, value)
                if alpha >= beta:
                    break
            
            return (column, value)