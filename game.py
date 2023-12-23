import random

import pygame
from pygame.locals import *


pygame.init()

# constants
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')


# load images
BACKGROUND_IMAGE = pygame.image.load('res/img/bg.png')
GROUND_IMAGE = pygame.image.load('res/img/ground.png')


# game loop
RUN = True
while RUN:

    # set screen background image
    screen.blit(BACKGROUND_IMAGE, (0, 0))

    # draw and scroll the ground
    screen.blit(GROUND_IMAGE, (0, SCREEN_HEIGHT - GROUND_IMAGE.get_height()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    # re-render screen with updates
    pygame.display.update()

pygame.quit()
