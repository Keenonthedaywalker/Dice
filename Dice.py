import pygame
import random

pygame.init()

(WIDTH, HEIGHT) = (800, 600)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

DICE = (300, 200, 200, 200)

TITLE = pygame.display.set_caption("Testing pygame in IDLE")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

randNum = random.randint(1, 6)

font = pygame.font.SysFont('arial', 20)

text = font.render("Do you want to Roll Again? Y/N", False, RED, WHITE)

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True        

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, DICE)
    
    
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

    SCREEN.blit(text, (300, 450))
            
    pygame.display.update()

pygame.quit()
