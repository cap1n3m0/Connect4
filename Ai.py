import random

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

#calls the other 3 winning functions (checkrow, checkcol, and checkDiagnol) and returns True if someone won
def hasWon(board, color):
    if checkRows(board, color) or checkColumns(board, color) or checkDiagonals(board, color):
        return True
    else:
        return False

#places the peice in whatever col they input
def placePiece(board, colour, col):
    col -= 1
    if not board[0][col] == "o":
        return False
    else:
        counter = 0
        for i in board:
            if not i[col] == "o":
                board[counter - 1][col] = colour
                
                return True
            counter += 1
        if board[5][col] == "o":
            board[5][col] = colour

# check to see if it is a vaild location to put things
def vaildLocation(board, col):
    col -= 1
    if not board[0][col] == "o":
        return False
    else:
        counter = 0
        for i in board:
            if not i[col] == "o":
                return True
            counter += 1
            
# Check for all of the 3 pairs of a color
def checkThree(board, piece):
    three_count = 0
    rowAmount = len(board)
    colAmount = len(board[0])
    emptyspaceChar = Ai.emptyspaceChar

    for r in range(rowAmount):
        for c in range(colAmount):
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
                if board[r][c] == board[r+1][c] == board[r+2][c] == piece and board[r+3][c] == emptyspaceChar:
                    three_count += 1
    
    return three_count

# Check for all of the 2 pairs of a color
def checkTwo(board, piece):
    twoCount = 0
    rowAmount = len(board)
    colAmount = len(board[0])
    emptyspaceChar = Ai.emptyspaceChar

    for r in range(rowAmount):
        for c in range(colAmount):
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
                if board[r][c] == board[r+1][c] == piece and board[r+2][c] == board[r+3][c] == emptyspaceChar:
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

    for col in range(colAmount):
        if vaildLocation(board, col):
            playableLocations.append(col)
    
    return playableLocations

# Calculate a score
def calculate_score(board, AIpiece, PLAYERpiece):
    threeScore = checkThree(board, AIpiece)
    twoScore = checkTwo(board, AIpiece)

    playerThreeScore = checkThree(board, PLAYERpiece)
    playerTwoScore = checkTwo(board, PLAYERpiece)

    score = threeScore + twoScore - playerThreeScore - playerTwoScore

    return score


class Ai:

    returnValue = 1000000000000
    emptyspaceChar = "o"

    def __init__(self, aiColor, playerColor):
        self.aiColor = aiColor
        self.playerColor = playerColor
        self.Pinfinity = float("inf")
        self.Ninfinity = float("-inf")
    
    def miMax(self, board, depth, alpha, beta, maximizingPlayer):
        playableLocations = findPlayableLocations(board)
        hasWonAi = hasWon(board, self.aiColor)
        hasWonPlayer = hasWon(board, self.playerColor)
        isTie = False

        terminal = True if hasWonAi or hasWonPlayer or isTie else False

        if depth == 0 or terminal:
            if terminal:
                if hasWonAi:
                    return (None, Ai.returnValue)
                elif hasWonPlayer:
                    return (None, -Ai.returnValue)
                
                else:
                    return (None, 0)
            else:
                return (None, calculate_score(board, self.aiColor, self.playerColor))
        
        if maximizingPlayer:
            value = self.Ninfinity
            column = random.choice(playableLocations)
            for col in playableLocations:
                temp_board = board
                placePiece(temp_board, self.aiColor, col)

                newScore = self.miMax(temp_board, depth-1, alpha, beta, False)[1]

                if newScore > value:
                    value = newScore
                    column = col
                
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            
            return (column, value)

        else:
            value = self.Pinfinity
            column = random.choice(playableLocations)
            for col in playableLocations:
                temp_board = board
                placePiece(temp_board, self.playerColor, col)

                newScore = self.miMax(temp_board, depth-1, alpha, beta, True)[1]

                if newScore < value:
                    value = newScore
                    column = col
                
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            
            return (column, value)


