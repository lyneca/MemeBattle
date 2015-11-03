__author__ = 'wing2048'
from classes import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
done = False
r = 0
g = 0
b = 0
increasing_color = 0
test_enemy = Enemy(10, 10, 10)
player = Player(50, 50, 10, True, PLAYER_1_CONTROLS)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    if increasing_color == 0:
        r += COLOUR_CHANGE_SPEED
        b -= COLOUR_CHANGE_SPEED
        if r == 100:
            increasing_color = 1
    if increasing_color == 1:
        g += COLOUR_CHANGE_SPEED
        r -= COLOUR_CHANGE_SPEED
        if g == 100:
            increasing_color = 2
    if increasing_color == 2:
        b += COLOUR_CHANGE_SPEED
        g -= COLOUR_CHANGE_SPEED
        if b == 100:
            increasing_color = 0
    pressed = pygame.key.get_pressed()
    enemies.update()
    players.update(pressed)
    trans_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    trans_overlay.set_alpha(100)
    trans_overlay.fill((r + 150, g + 150, b + 150, 0))
    screen.blit(trans_overlay, (0, 0))
    enemies.draw(screen)
    players.draw(screen)
    pygame.display.flip()
    clock.tick(60)