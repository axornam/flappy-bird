import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for n in range(1, 4):
            image = pygame.image.load(f"res/img/bird{n}.png")
            self.images.append(image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.velocity = 0
        self.jumped = False

    def update(self, event: pygame.event.Event = None, flying: bool = False, game_over: bool = False):

        # add gravity to bring bird down
        if flying:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8

            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)

        if not game_over:
            # add jumping
            if event is not None:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.jumped == False:
                        self.jumped = True
                        self.velocity = -10
                if event.type == pygame.KEYUP:
                    self.jumped = False

            # handle flappy animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            # rotate bird
            self.image = pygame.transform.rotate(
                self.images[self.index], self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
