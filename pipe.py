import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position, pipe_gap: int = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"res/img/pipe.png")
        self.rect = self.image.get_rect()

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self, SCROLL_SPEED: int = 0):
        self.rect.x -= SCROLL_SPEED
