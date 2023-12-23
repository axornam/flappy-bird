import pygame


class Button():

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen: pygame.surface.Surface = None, *args, **kwargs):
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
