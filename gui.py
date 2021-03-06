import pygame
import random
import AiStuff.Ai as Ai
from AiStuff.MainAi import *
from Player import Player


class Color:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)


class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.active = False
        self.radius = 40

    def draw(self, win):
        '''
        win is going to be the window to display 
        the piece onto.

        center is going to be the center of the 
        piece that is going to be drawnn onto the 
        win.'''
        if self.active is True:
            pygame.draw.circle(win, self.color, self.pos, self.radius)


def setCords(): 
    x = 167
    y = 210
    spacingX = 53
    spacingY = 4
    cords = []
    for i in range(6):
        cords.append([])
        for l in range(7):
            cords[i].append((x, y))
            x += 38 + spacingX

        x = 167
        y += (38*2) + spacingY

    return cords

def showPieceOnMouse(mousePos, win, color, radius):
    if mousePos[0] < 130:
        pygame.draw.circle(win, color, (130, 130), radius)
    elif mousePos[0] > 745:
        pygame.draw.circle(win, color, (745, 130), radius)
    else:
        pygame.draw.circle(win, color, (mousePos[0], 130), radius)

def getXPosBounds(cords):
    xRanges = {}
    temp = []

    for pos in cords[0]:
        x = pos[0]
        temp.append(x-38)

    i = 0
    while len(temp) > 0:
        if i > 0:
            xRanges[i] = [xRanges[i-1][1], temp[0]]
            i += 1
            temp.pop(0)
        else:
            xRanges[i] = [temp[0]-38, temp[1]]
            i += 1
            temp.pop(0)
            temp.pop(0)
    
    xRanges[i] = [xRanges[i-1][1], 745]
    
    return xRanges

def getRowPos(mousePos, bounds):
    X = mousePos[0]
    if 130 < X < 745:
        for i in range(len(bounds)):
            if bounds[i][0] < X < bounds[i][1]:
                return i + 1
    else:
        return False

def drawWindow(win, pieces):
    # draw the pieces
    for row in pieces:
        for piece in row:
            piece.draw(win)

def turnOnPiece(board, pieces):
    for rowNum, row in enumerate(board):
        for colNum, col in enumerate(row):
            if col == "r":
                if pieces[rowNum][colNum].active is False:
                    pieces[rowNum][colNum].active = True
                    pieces[rowNum][colNum].color = (255, 0, 0)
            elif col == "y":
                if pieces[rowNum][colNum].active is False:
                    pieces[rowNum][colNum].active = True
                    pieces[rowNum][colNum].color = (255, 255, 0)
            elif col == "o":
                if pieces[rowNum][colNum].active is True:
                    pieces[rowNum][colNum].active = False

def dropPiece(col, cords, board, color, rowInDrop, active):
    # change the y pos of the piece until it reaches anothjer piece or the bottom
    
    # vaildMoves = [0, 1, 2, 3, 4, 5]
    vaildMoves = Ai.findPlayableLocations(board)

    if col in vaildMoves:
        # y pos changing
        pos = cords[rowInDrop][col]
        if active:
            if board[rowInDrop][col] == "o":
                board[rowInDrop][col] = color
            else:
                # im done
                return True
        else:
            if board[rowInDrop][col] == "r" or board[rowInDrop][col] == "y":
                board[rowInDrop][col] = color
            else:
                return True


def main(AiYN=False):

    board = [
        ["o", "o", "o", "o", "o", "o", "o"],
        ["o", "o", "o", "o", "o", "o", "o"],
        ["o", "o", "o", "o", "o", "o", "o"],
        ["o", "o", "o", "o", "o", "o", "o"],
        ["o", "o", "o", "o", "o", "o", "o"],
        ["o", "o", "o", "o", "o", "o", "o"]
    ]

    coords = setCords()
    bounds = getXPosBounds(coords)
    
    # pygame window setup
    SIZE = (900, 900)
    WIN = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    pygame.font.init()

    # Loading img
    cwd = os.getcwd()
    path = os.path.join(cwd, "Connect4", "Connect4Board.png") if "Connect4" not in cwd else os.path.join(cwd, "Connect4Board.png")
    boardImg = pygame.image.load(path)


    playerturn = True
    if AiYN is False:
        Player1 = Player("r")
        Player2 = Player("y")
        currentPlayer = Player1
        lastPlayer = False
    else:
        AiPiece = Ai.Ai(aiColor="r", playerColor="y")
        Player2 = Player("y")
        currentPlayer = AiPiece

    run = True
    mousePos = pygame.mouse.get_pos()

    pieces = []
    for row in coords:
        temp = []
        for col in row:
            piece = Piece(Color.RED, (col[0], col[1]))
            temp.append(piece)
        pieces.append(temp)

    FPS = 60
    # Game loop
    while run:
        clock.tick(FPS)

        # clear the screen
        WIN.fill((255, 255, 255))

        # get teh mouse pos
        mousePos = pygame.mouse.get_pos()

        # Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                # if it is the users turn then place piece
                if AiYN is False:
                    col = getRowPos(pygame.mouse.get_pos(), bounds)
                    if col is not False:
                        # If its player turn then drop piece
                        result = placePiece(board, currentPlayer.color, col)
                        if result is False:
                            num = random.randint(-1, 1)
                            while result is False:
                                result = placePiece(board, currentPlayer.color, col+num)
                        currentPlayer = Player2 if currentPlayer is Player1 else Player1
                
                else:
                    if currentPlayer is Player2:
                        col = getRowPos(pygame.mouse.get_pos(), bounds)
                        if col is not False and col is not None:
                            # If its player turn then drop piece
                            result = placePiece(board, currentPlayer.color, col)
                            if result is False:
                                num = random.randint(-1, 1)
                                while result == False:
                                    result = placePiece(board, currentPlayer.color, col+num)
                            
                            currentPlayer = AiPiece
        
        # game logic
            
        if AiYN is False:
            if playerturn:
                color = (255, 0, 0) if currentPlayer.color == "r" else (255, 255, 0)
                showPieceOnMouse(mousePos, WIN, color, 38)
            else:
                color = (255, 0, 0) if currentPlayer.color == "r" else (255, 255, 0)
                showPieceOnMouse(mousePos, WIN, color, 38)
                
            playerturn = not playerturn

        elif AiYN:
            if currentPlayer is AiPiece:
                xPos = AiPiece.minMax(board, 5, float("-inf"), float("inf"), True)[0]
                result = placePiece(board, AiPiece.color, xPos)
                if result is False:
                    num = random.randint(-1, 1)
                    while result == False:
                        result = placePiece(board, currentPlayer.color, xPos+num)
                currentPlayer = Player2
            
            else:
                showPieceOnMouse(mousePos, WIN, (255, 255, 0), 38)
                
        # Displaying the screen
        
        # Turn on all pieces that need to be turned on based off the board
        turnOnPiece(board, pieces)
        drawWindow(WIN, pieces)
        WIN.blit(boardImg, (120, 170))
        pygame.display.update()           
