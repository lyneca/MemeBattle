__author__ = 'wing2048'
import random

from constants import *


enemies = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, s, rc):
        self.image = pygame.Surface((s, s))
        self.image.fill((0, 0, 0))
        self.random_colours = rc
        self.rect = pygame.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        enemies.add(self)

    def update(self):
        if self.random_colours:
            c = random.randint(1, 3)
            p = random.randint(0, 255)
            f = random.randint(0, 150)
            if c == 1:
                self.image.fill((p, f, f))
            elif c == 2:
                self.image.fill((f, p, f))
            else:
                self.image.fill((f, f, p))


class Player(pygame.sprite.Sprite):
    def __init__(self, s, rc):
        self.image = pygame.Surface((s, s))
        self.image.fill((0, 0, 0))
        self.random_colours = rc
        self.rect = pygame.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        enemies.add(self)