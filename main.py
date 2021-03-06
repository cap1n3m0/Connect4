from Player import Player
import AiStuff.Ai as Ai
from one import *
import pygame

class Button():
    def __init__(self, color, x, y, width, height, text='', function=None, args=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.function = function
        self.args = args

    def draw(self,  win, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            pygame.font.init()
            font = pygame.font.SysFont('comicsans', 30)# 30 is Font size < ------------------------------------
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

Buttons = []

SIZE = (900, 1100)
win = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
run = True
aiButton = Button(
    (255, 255, 255),
    0,  # x
    70, # y
    100,
    50,
    "AI vs You"
)

oneButton = Button(
    (255, 255, 255),
    0, # x
    0, # y
    100,
    50,
    "1 V 1"
)

FPS = 60
while run:
    win.fill((255, 255, 255))
    clock.tick(FPS)
    
    # check what button was pressed
    mousePos = pygame.mouse.get_pos()
    
    # pygame event check

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Buttons:
                if button.isover(mousePos):
                    if button.function != None:
                        button.function(button.args) if button.args != None else button.function()


    
    # Fill the screen with white
    win.fill((255, 255, 255))
    
    # Draw buttons
    #aiButton.draw(win)
    oneButton.draw(win)

    # update the display
    pygame.display.update()
    