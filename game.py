import random

import pygame
from pygame.locals import *


pygame.init()

# constants
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

clock = pygame.time.Clock()
FPS = 60


# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# load images
BACKGROUND_IMAGE = pygame.image.load('res/img/bg.png')
GROUND_IMAGE = pygame.image.load('res/img/ground.png')

# game variables
BG_1_SCROLL = 0
BG_2_SCROLL = BACKGROUND_IMAGE.get_width()
SCROLL_SPEED = 4

# game loop
RUN = True
while RUN:
    # frame-rate
    clock.tick(FPS)

    BG_1_SCROLL -= SCROLL_SPEED
    BG_2_SCROLL -= SCROLL_SPEED

    # set and scroll screen background and floor images
    screen.blit(BACKGROUND_IMAGE, (BG_1_SCROLL, 0))
    screen.blit(GROUND_IMAGE, (BG_1_SCROLL, SCREEN_HEIGHT -
                GROUND_IMAGE.get_height()))

    # set and scroll second screen background and floor
    # images after the first leaves the screen
    screen.blit(BACKGROUND_IMAGE,
                (BG_2_SCROLL, 0))
    screen.blit(GROUND_IMAGE,
                (BG_2_SCROLL, SCREEN_HEIGHT -
                 GROUND_IMAGE.get_height()))

    # poll events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    # scroll background UI
    if BG_1_SCROLL < BACKGROUND_IMAGE.get_width() * -1:
        BG_1_SCROLL = BACKGROUND_IMAGE.get_width()

    if BG_2_SCROLL < BACKGROUND_IMAGE.get_width() * -1:
        BG_2_SCROLL = BACKGROUND_IMAGE.get_width()
        # GROUND_SCROLL = 0

    # re-render screen with updates
    pygame.display.update()

pygame.quit()
