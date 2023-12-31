import random

from bird import Bird
from button import Button
from pipe import Pipe
import pygame
from pygame.locals import *
from utils import draw_text


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

FONT = pygame.font.SysFont('FiraCode Nerd Font', 90, bold=True)
WHITE = (255, 255, 255)

# load images
BACKGROUND_IMAGE = pygame.image.load('res/img/bg.png')
GROUND_IMAGE = pygame.image.load('res/img/ground.png')
BUTTON_IMAGE = pygame.image.load('res/img/restart.png')

# game variables
BG_1_SCROLL = 0
BG_2_SCROLL = BACKGROUND_IMAGE.get_width()
SCROLL_SPEED = 4
FLYING = False
GAME_OVER = False
PIPE_GAP = 150
PIPE_FREQ = 1500  # milliseconds
last_pipe = pygame.time.get_ticks() - PIPE_FREQ

SCORE = 0
PASS_PIPE = False
RESTART = False


bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(SCREEN_HEIGHT / 2))
bird_group.add(flappy)

restart_button = Button(SCREEN_WIDTH // 2 - 50,
                        SCREEN_HEIGHT // 2 - 100, BUTTON_IMAGE)


def restart_game():
    global SCORE, GAME_OVER, FLYING
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = SCREEN_HEIGHT // 2
    SCORE = 0
    GAME_OVER = False
    FLYING = False


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
            elif e.key == pygame.K_y and GAME_OVER == True:
                restart_game()
            elif e.key == pygame.K_n and GAME_OVER == True:
                RUN = False

    # check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left:
            if bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right:
                if PASS_PIPE == False:
                    PASS_PIPE = True
        if PASS_PIPE == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                SCORE += 1
                PASS_PIPE = False

    # collision detection
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        GAME_OVER = True

    # check if bird has hit the ground
    if flappy.rect.bottom > 768:
        GAME_OVER = True
        FLYING = False

    if not GAME_OVER and not FLYING:
        draw_text('PRESS ENTER', FONT, screen, WHITE, int(
            SCREEN_WIDTH / 2 - FONT.size('PRESS ENTER')[0] / 2
        ), int(SCREEN_HEIGHT / 3))

    elif not GAME_OVER and FLYING:
        # draw scores
        draw_text(str(SCORE), FONT, screen, WHITE, int(SCREEN_WIDTH / 2), 0)

        # generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > PIPE_FREQ:
            pipe_height = random.randint(-100, 100)
            top_pipe = Pipe(SCREEN_WIDTH, int(
                SCREEN_HEIGHT / 2) + pipe_height, 1, pipe_gap=PIPE_GAP)
            bottom_pipe = Pipe(
                SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipe_height, -1, pipe_gap=PIPE_GAP)
            pipe_group.add(top_pipe)
            pipe_group.add(bottom_pipe)

            last_pipe = time_now

        # scroll background UI
        BG_1_SCROLL -= SCROLL_SPEED
        BG_2_SCROLL -= SCROLL_SPEED

        if BG_1_SCROLL < BACKGROUND_IMAGE.get_width() * -1:
            BG_1_SCROLL = BACKGROUND_IMAGE.get_width()

        if BG_2_SCROLL < BACKGROUND_IMAGE.get_width() * -1:
            BG_2_SCROLL = BACKGROUND_IMAGE.get_width()
            # GROUND_SCROLL = 0

        pipe_group.update(SCROLL_SPEED)

    elif GAME_OVER == True:
        draw_text(f"HIGH SCORE: {SCORE}", FONT, screen, WHITE, int(
            SCREEN_WIDTH / 2 - FONT.size(f"HIGH SCORE: {SCORE}")[0] / 2
        ), int(SCREEN_HEIGHT / 6))

        draw_text('GAME OVER', FONT, screen, WHITE, int(
            SCREEN_WIDTH / 2 - FONT.size('GAME OVER')[0] / 2), int(SCREEN_HEIGHT / 3))
        draw_text('RESTART ? y/n', FONT, screen,
                  WHITE, int(SCREEN_WIDTH / 2 - FONT.size('RESTART ? y/n')[0] / 2), int(SCREEN_HEIGHT / 2))

        # restart_button.draw(screen)

    bird_group.update(event, flying=FLYING, game_over=GAME_OVER)

    # re-render screen with updates
    pygame.display.update()

pygame.quit()
