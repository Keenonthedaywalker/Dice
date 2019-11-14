import pygame
import random

from UIComponents import *

pygame.init()

(WIDTH, HEIGHT) = (800, 600)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

DICE = (300, 200, 200, 200)

TITLE = pygame.display.set_caption("Testing pygame in IDLE")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

randNum = random.randint(1, 6)

def click():
    if button.color == GREEN:
        button.color = RED
    else:
        button.color = GREEN


button_clicked = False

button = Button((350, 450, 100, 50), (0, 0), GREEN, 255,  "Re-Roll", font_size=10,  click_function=click)

def butTrue():

    button
    button_clicked = True


def die():
    if randNum == 1:
        pygame.draw.circle(SCREEN, RED, (400, 300), 10)
    elif randNum == 2:
        pygame.draw.circle(SCREEN, RED, (365, 300), 10)
        pygame.draw.circle(SCREEN, RED, (435, 300), 10)
    elif randNum == 3:
        pygame.draw.circle(SCREEN, RED, (330, 230), 10)
        pygame.draw.circle(SCREEN, RED, (395, 290), 10)
        pygame.draw.circle(SCREEN, RED, (460, 360), 10)
    elif randNum == 4:
        pygame.draw.circle(SCREEN, RED, (330, 260), 10)
        pygame.draw.circle(SCREEN, RED, (330, 350), 10)
        pygame.draw.circle(SCREEN, RED, (460, 260), 10)
        pygame.draw.circle(SCREEN, RED, (460, 350), 10)
    elif randNum == 5:
        pygame.draw.circle(SCREEN, RED, (330, 260), 10)
        pygame.draw.circle(SCREEN, RED, (330, 350), 10)
        pygame.draw.circle(SCREEN, RED, (460, 260), 10)
        pygame.draw.circle(SCREEN, RED, (460, 350), 10)
        pygame.draw.circle(SCREEN, RED, (393, 309), 10)
    elif randNum == 6:
        pygame.draw.circle(SCREEN, RED, (330, 260), 10)
        pygame.draw.circle(SCREEN, RED, (330, 350), 10)
        pygame.draw.circle(SCREEN, RED, (460, 260), 10)
        pygame.draw.circle(SCREEN, RED, (460, 350), 10)
        pygame.draw.circle(SCREEN, RED, (393, 260), 10)
        pygame.draw.circle(SCREEN, RED, (393, 350), 10)

    

    

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.clicked(pygame.mouse.get_pos()):
                print('clicked')

        if button_clicked == True:
            for i in range(1):
                die()

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, DICE)
    
  
    die()
    butTrue()       
    button.draw(SCREEN)
    pygame.display.update()

pygame.quit()
