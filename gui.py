import pygame
import random
import AiStuff.Ai as Ai
from AiStuff.MainAi import *
from Player import Player


class Color:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)


def setCords(): 
    x = 165
    y = 205
    spacing = 53
    cords = []
    for i in range(6):
        cords.append([])
        for l in range(7):
            cords[i].append((x, y))
            x += 38 + spacing

        x = 164
        y += 80

    return cords

class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.active = False
        self.radius = 38

    def draw(self, win):
        '''
        win is going to be the window to display 
        the piece onto.

        center is going to be the center of the 
        piece that is going to be drawnn onto the 
        win.'''
        if self.active is True:
            pygame.draw.circle(win, self.color, self.pos, self.radius)

#                    (x, y) surface (r,g,b) radius
def showPieceOnMouse(mousePos, win, color, radius):
    if mousePos[0] < 165:
        pygame.draw.circle(win, color, (165, 130), radius)
    elif mousePos[0] > 745:
        pygame.draw.circle(win, color, (745, 130), radius)
    else:
        pygame.draw.circle(win, color, (mousePos[0], 130), radius)


def getXPosBounds(cords):
    xRanges = {}
    temp = []

    for pos in cords[0]:
        x = pos[0]
        temp.append(x)

    i = 0
    while len(temp) > 2:
        xRanges[i] = [temp[0], temp[1]]
        i += 1
        temp.pop(0)
        temp.pop(0)
    
    return xRanges

def getRowPos(mousePos, bounds):
    X = mousePos[0]
    for i in range(len(bounds)):
        if bounds[i][0] < X < bounds[i][1]:
            return i + 1

def drawWindow(win, pieces):
    # Fill the background
    win.fill(Color.WHITE)

    for piece in pieces:
        piece.draw(win)
    
    # Update the screen
    pygame.display.update()

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
    coords = setCords()
    bounds = getXPosBounds(coords)
    
    SIZE = (900, 1100)
    WIN = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    FONT = pygame.font.init()
    boardImg = pygame.image.load("Connect4Board.png")   
    playerturn = True
    if AiYN is False:
        Player1 = Player("r")
        Player2 = Player("y")
        currentPlayer = Player1
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
        mousePos = pygame.mouse.get_pos()

        # Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if it is the users turn then place piece
                
                col = getRowPos(pygame.mouse.get_pos(), bounds)
                # If its player turn then drop piece
                result = placePiece(board, currentPlayer.color, col)
                while result is False:
                    num = random.randint(-1, 1)
                    result = placePiece(board, currentPlayer.color, col+num)
                
                # if it is not users turn then place othr piece
        
        # game logic
            
        if AiYN is False:
            if playerturn:
                showPieceOnMouse(mousePos, WIN, Color.RED, 38)
                currentPlayer = Player2
            else:
                
                currentPlayer = Player1
                
            playerturn = not playerturn

        elif AiYN:
            if currentPlayer is AiPiece:
                xPos = AiPiece.minMax(board, 5, float("-inf"), float("inf"), True)[0]
                result = placePiece(board, AiPiece.color, xPos)
                if result == False:
                    xPos += 1
                    result = placePiece(board, AiPiece.color, xPos)
                currentPlayer = Player2
            
            else:
                showPieceOnMouse(mousePos, WIN, Color.YELLOW, 38)
                dropPiece()
                # player 2 things

                currentPlayer = Player2
        '''
        if not hasWon(board, 'r'):
            currentPlayer = playerYellow
            print("Player yellow, choose a position: ")
            xPos = int(input())
            placePiece(board, currentPlayer.color, xPos)
            if hasWon(board, "y"):
                print("You Won")
        else:
            print("You lost!\nBetter Luck next time!\n")
            break
            '''
            
            
                
        # Displaying the screen
        WIN.fill((255, 255, 255))

        #               mousePos, win, color, radius
        showPieceOnMouse(mousePos, WIN, Color.RED, 38)
        
        turnOnPiece(board, pieces)
        WIN.blit(boardImg, (120, 170))
        pygame.display.update()           
