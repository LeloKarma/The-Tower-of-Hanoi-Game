import pygame
import sys

#init
pygame.init()

#set up screen dims
SCREEN_WIDTH = 800
SCREEN_LENGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
pygame.display.set_caption("My Pygame Project")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the screen
    screen.fill(WHITE)

    #draw a black rect in the center of the screen
    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH/2 - 50, SCREEN_LENGTH/2 - 50, 100, 100))


    #update display
    pygame.display.flip()

#Lets quit
pygame.quit()
sys.exit()
    