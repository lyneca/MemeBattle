import math

__author__ = 'wing2048'
import random

from constants import *


enemies = pygame.sprite.Group()
players = pygame.sprite.Group()


def cap(n, c):
    return c if n >= c else n


def limit(n, l, u):
    return u if n >= u else l if n <= l else n


class Game:
    def __init__(self):
        self.time_scale = 1
        self.overlay_size = OVERLAY_SIZE
        self.overlay = pygame.Surface((self.overlay_size, self.overlay_size))
        self.overlay_rect = self.overlay.get_rect()
        self.overlay.set_alpha(1)
        self.overlay_alpha = 100

    def slow(self, amount):
        self.time_scale = amount

    def reset_small_overlay(self):
        self.overlay_size = PLAYER_SIZE
        self.overlay = pygame.Surface((self.overlay_size, self.overlay_size))
        self.overlay_rect = self.overlay.get_rect()
        self.overlay.set_alpha(100)
        self.overlay_alpha = 100

    def reset_overlay(self):
        self.overlay_size = OVERLAY_SIZE
        self.overlay = pygame.Surface((self.overlay_size, self.overlay_size))
        self.overlay_rect = self.overlay.get_rect()
        self.overlay.set_alpha(1)
        self.overlay_alpha = 1

    def update(self):
        self.overlay = pygame.Surface((self.overlay_rect.width, self.overlay_rect.height))
        self.overlay.set_alpha(self.overlay_alpha)


game = Game()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, s, rc=True):
        self.image = pygame.Surface((s, s))
        self.image.fill((0, 0, 0))
        self.random_colours = rc
        self.rect = self.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        enemies.add(self)

        self.direction = 0

        self.increasing_color = random.randint(0, 2)
        self.color_timer = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

        self.rect.x = self.x
        self.rect.y = self.y

    def move_random(self):
        self.direction = random.randint(0, 3)
        if self.direction == 0:
            self.vy = -random.randint(1, ENEMY_MOVE_AMOUNT)
        elif self.direction == 1:
            self.vy = random.randint(1, ENEMY_MOVE_AMOUNT)
        elif self.direction == 2:
            self.vx = -random.randint(1, ENEMY_MOVE_AMOUNT)
        else:
            self.vx = random.randint(1, ENEMY_MOVE_AMOUNT)

    def update(self):
        self.vx *= 0.98
        self.vy *= 0.98
        if self.random_colours:
            if self.increasing_color == 0:
                self.r += ENEMY_COLOUR_CHANGE_SPEED * game.time_scale
                self.b -= ENEMY_COLOUR_CHANGE_SPEED * game.time_scale
                if self.r >= 100:
                    self.increasing_color = 1
            if self.increasing_color == 1:
                self.g += ENEMY_COLOUR_CHANGE_SPEED * game.time_scale
                self.r -= ENEMY_COLOUR_CHANGE_SPEED * game.time_scale
                if self.g >= 100:
                    self.increasing_color = 2
            if self.increasing_color == 2:
                self.b += ENEMY_COLOUR_CHANGE_SPEED * game.time_scale
                self.g -= ENEMY_COLOUR_CHANGE_SPEED * game.time_scale
                if self.b >= 100:
                    self.increasing_color = 0
            self.image.fill((
                limit(self.r + 150, 0, 255),
                limit(self.g + 150, 0, 255),
                limit(self.b + 150, 0, 255)
            ))
        if abs(self.vx) + abs(self.vy) < 1:
            self.move_random()
        self.x += self.vx * abs(game.time_scale)
        self.y += self.vy * abs(game.time_scale)
        if self.y < 20:
            self.vy = 2
        elif self.y > SCREEN_HEIGHT - 20:
            self.vy = -2
        elif self.x < 20:
            self.vx = 2
        elif self.x > SCREEN_WIDTH - 20:
            self.vx = -2
        self.rect.x = self.x
        self.rect.y = self.y


def get_distance(s1, s2):
    return math.sqrt((s1.x - s2.x) ** 2 + (s1.y - s2.y) ** 2)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, s, mouse, controls):
        self.mouse = mouse
        if not self.mouse:
            self.key_up = controls['up']  # dictionary keys are strings for easy modding
            self.key_down = controls['down']
            self.key_left = controls['left']
            self.key_right = controls['right']
        self.size = s
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
        collide = pygame.sprite.spritecollide(self, enemies, False)
        for sprite in collide:
            print('dieded')
        # flag = False
        # for enemy in enemies:
        #     if get_distance(self, enemy) < 50:
        #         flag = True
        #         game.slow(0.7)
        #         break
        # if not flag:
        #     game.time_scale = 1

        if not self.mouse:
            for ku in self.key_up:
                if pressed[ku]:
                    self.vy -= PLAYER_ACCELERATE_Y
            for kd in self.key_down:
                if pressed[kd]:
                    self.vy += PLAYER_ACCELERATE_Y
            for kl in self.key_left:
                if pressed[kl]:
                    self.vx -= PLAYER_ACCELERATE_X
            for kr in self.key_right:
                if pressed[kr]:
                    self.vx += PLAYER_ACCELERATE_X
            self.vx *= 0.96
            self.vy *= 0.96
            self.x += self.vx
            self.y += self.vy
        else:
            self.x, self.y = pygame.mouse.get_pos()
        self.rect.x = self.x
        self.rect.y = self.y