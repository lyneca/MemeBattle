__author__ = 'wing2048'
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOUR_CHANGE_SPEED = 1
ENEMY_COLOUR_CHANGE_SPEED = 20
PLAYER_ACCELERATE_X = 0.5
PLAYER_ACCELERATE_Y = 0.5

PLAYER_1_CONTROLS = {
    'up': [pygame.K_w, pygame.K_UP],
    'down': [pygame.K_s, pygame.K_DOWN],
    'left': [pygame.K_a, pygame.K_LEFT],
    'right': [pygame.K_d, pygame.K_RIGHT],
}