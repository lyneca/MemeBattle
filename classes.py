__author__ = 'wing2048'
import random

from constants import *


enemies = pygame.sprite.Group()
players = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, s, rc=True):
        self.image = pygame.Surface((s, s))
        self.image.fill((0, 0, 0))
        self.random_colours = rc
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.sprite.Sprite.__init__(self)
        enemies.add(self)

        self.increasing_color = 0
        self.color_timer = 0
        self.r = 0
        self.g = 0
        self.b = 0

    def update(self):
        if self.random_colours:
            if self.increasing_color == 0:
                self.r += ENEMY_COLOUR_CHANGE_SPEED
                self.b -= ENEMY_COLOUR_CHANGE_SPEED
                if self.r == 100:
                    self.increasing_color = 1
            if self.increasing_color == 1:
                self.g += ENEMY_COLOUR_CHANGE_SPEED
                self.r -= ENEMY_COLOUR_CHANGE_SPEED
                if self.g == 100:
                    self.increasing_color = 2
            if self.increasing_color == 2:
                self.b += ENEMY_COLOUR_CHANGE_SPEED
                self.g -= ENEMY_COLOUR_CHANGE_SPEED
                if self.b == 100:
                    self.increasing_color = 0
            self.image.fill((self.r + 150, self.g + 150, self.b + 150))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, s, controls):
        self.key_up = controls['up']  # dictionary keys are strings for easy modding
        self.key_down = controls['down']
        self.key_left = controls['left']
        self.key_right = controls['right']

        self.image = pygame.Surface((s, s))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        pygame.sprite.Sprite.__init__(self)
        players.add(self)

    def update(self, pressed):
        for ku in self.key_up:
            if pressed[ku]:
                self.vy += -PLAYER_ACCELERATE_Y
        for kd in self.key_down:
            if pressed[kd]:
                self.vy += PLAYER_ACCELERATE_Y
        for kl in self.key_left:
            if pressed[kl]:
                self.vx += -PLAYER_ACCELERATE_X
        for kr in self.key_right:
            if pressed[kr]:
                self.vx += PLAYER_ACCELERATE_X
        self.vx *= 0.96
        self.vy *= 0.96
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.rect.y = self.y