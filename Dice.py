#imports modules 
import pygame
import random

#imports kubapilch's PygameUIComponents Module
from UIComponents import *

#Initializes pygame
pygame.init()

#Width and Height for the Screen
(WIDTH, HEIGHT) = (800, 600)

#Colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Dice width, height, xpos, and ypos
DICE = (300, 200, 200, 200)

#Title of game
TITLE = pygame.display.set_caption("Testing pygame in IDLE")
#The game window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#Generats random number between 1 and 6 
randNum = random.randint(1, 6)

#Creates a function that turns the button Red and Green 
def click():
   
    if button.color == GREEN:
        button.color = RED
    else:
        button.color = GREEN
#Creates a button from kubapilch's module 
button = Button((350, 450, 100, 50), (0, 0), GREEN, 255,  "Re-Roll", font_size=10,  click_function=click)

#Creates a function for the dice logic
def die(num):
    if num == 1:
        pygame.draw.circle(SCREEN, RED, (400, 300), 10)
    elif num == 2:
        pygame.draw.circle(SCREEN, RED, (365, 300), 10)
        pygame.draw.circle(SCREEN, RED, (435, 300), 10)
    elif num == 3:
        pygame.draw.circle(SCREEN, RED, (330, 230), 10)
        pygame.draw.circle(SCREEN, RED, (395, 290), 10)
        pygame.draw.circle(SCREEN, RED, (460, 360), 10)
    elif num == 4:
        pygame.draw.circle(SCREEN, RED, (330, 260), 10)
        pygame.draw.circle(SCREEN, RED, (330, 350), 10)
        pygame.draw.circle(SCREEN, RED, (460, 260), 10)
        pygame.draw.circle(SCREEN, RED, (460, 350), 10)
    elif num == 5:
        pygame.draw.circle(SCREEN, RED, (330, 260), 10)
        pygame.draw.circle(SCREEN, RED, (330, 350), 10)
        pygame.draw.circle(SCREEN, RED, (460, 260), 10)
        pygame.draw.circle(SCREEN, RED, (460, 350), 10)
        pygame.draw.circle(SCREEN, RED, (393, 309), 10)
    elif num == 6:
        pygame.draw.circle(SCREEN, RED, (330, 260), 10)
        pygame.draw.circle(SCREEN, RED, (330, 350), 10)
        pygame.draw.circle(SCREEN, RED, (460, 260), 10)
        pygame.draw.circle(SCREEN, RED, (460, 350), 10)
        pygame.draw.circle(SCREEN, RED, (393, 260), 10)
        pygame.draw.circle(SCREEN, RED, (393, 350), 10)
 
   
#Used fo the main game loop
gameExit = False

#Main game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
 
        #If the mouse button is clicked do the following:
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Get the mouse position
            if button.clicked(pygame.mouse.get_pos()):
                #Regenarates a random number
                randNum = random.randint(1, 6)

    #Fills the screen with the color black
    SCREEN.fill(BLACK)
    #Drawing the dice
    pygame.draw.rect(SCREEN, WHITE, DICE)
    #Drawing the dice numbers
    die(randNum)

    #Draws the button to the screen
    button.draw(SCREEN)
    #Updates the graphics
    pygame.display.update()

#Lets the user quit when the X button is clicked
pygame.quit()

