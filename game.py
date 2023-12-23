import random

from bird import Bird
from pipe import Pipe
import pygame
from pygame.locals import *


pygame.init()

# constants
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

clock = pygame.time.Clock()
event = None
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
FLYING = False
GAME_OVER = False
PIPE_GAP = 150

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(SCREEN_HEIGHT / 2))
bird_group.add(flappy)

top_pipe = Pipe(300, int(SCREEN_HEIGHT / 2), 1, pipe_gap=PIPE_GAP)
bottom_pipe = Pipe(300, int(SCREEN_HEIGHT / 2), -1, pipe_gap=PIPE_GAP)
pipe_group.add(top_pipe)
pipe_group.add(bottom_pipe)

# game loop
RUN = True
while RUN:
    # frame-rate
    clock.tick(FPS)

    # set and scroll screen background and floor images
    screen.blit(BACKGROUND_IMAGE, (BG_1_SCROLL, 0))
    screen.blit(BACKGROUND_IMAGE,
                (BG_2_SCROLL, 0))

    # draw bird group
    bird_group.draw(screen)
    pipe_group.draw(screen)

    # images after the first leaves the screen
    screen.blit(GROUND_IMAGE, (BG_1_SCROLL, SCREEN_HEIGHT -
                GROUND_IMAGE.get_height()))
    screen.blit(GROUND_IMAGE,
                (BG_2_SCROLL, SCREEN_HEIGHT -
                 GROUND_IMAGE.get_height()))

    # poll events
    for e in pygame.event.get():
        event = e
        if e.type == pygame.QUIT:
            RUN = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                RUN = False
            elif e.key == pygame.K_RETURN and FLYING == False and GAME_OVER == False:
                FLYING = True

    # check if bird has hit the ground
    if flappy.rect.bottom > 768:
        GAME_OVER = True
        FLYING = False

    if not GAME_OVER:
        BG_1_SCROLL -= SCROLL_SPEED
        BG_2_SCROLL -= SCROLL_SPEED

        # scroll background UI
        if BG_1_SCROLL < BACKGROUND_IMAGE.get_width() * -1:
            BG_1_SCROLL = BACKGROUND_IMAGE.get_width()

        if BG_2_SCROLL < BACKGROUND_IMAGE.get_width() * -1:
            BG_2_SCROLL = BACKGROUND_IMAGE.get_width()
            # GROUND_SCROLL = 0

    bird_group.update(event, flying=FLYING, game_over=GAME_OVER)
    pipe_group.update(SCROLL_SPEED)

    # re-render screen with updates
    pygame.display.update()

pygame.quit()
