import gui
import pygame
import time

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
        print(pos)
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


def switchToAi():
    run = False
    pygame.display.quit()
    time.sleep(0.3)
    gui.main(AiYN=True)


def switchToPlayer():
    run = False 
    pygame.display.quit()
    time.sleep(0.3)
    gui.main(AiYN=False)

Buttons = []

SIZE = (800, 800)
win = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
run = True
aiButton = Button(
    (255, 255, 255),
    int(SIZE[0]/2 - 50),  # x
    int(SIZE[1]/2 + 35), # y
    100,
    50,
    "AI vs You",
    function=switchToAi
)
Buttons.append(aiButton)

oneButton = Button(
    (255, 255, 255),    
    int(SIZE[0]/2 - 50), # x
    int(SIZE[1]/2 - 35), # y
    100,
    50,
    "1 V 1",
    function=switchToPlayer
)
Buttons.append(oneButton)

FPS = 60
while run:
    win.fill((255, 255, 255))
    clock.tick(FPS)
    
    # check what button was pressed
   
    
    # pygame event check

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #mousePos = pygame.mouse.get_pos()
            for button in Buttons:
                if button.isOver(pygame.mouse.get_pos()):
                    if button.function != None:
                        button.function(button.args) if button.args != None else button.function()


    
    # Fill the screen with white
    win.fill((255, 255, 255))
    
    # Draw buttons
    aiButton.draw(win, (0, 0, 0))
    oneButton.draw(win, (0, 0, 0))

    # update the display
    pygame.display.update()
    