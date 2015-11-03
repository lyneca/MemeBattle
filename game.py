__author__ = 'wing2048'
from classes import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
done = False
r = 0
g = 0
b = 200
increasing_color = 0
for i in range(80):
    Enemy(400, 300, 10)
player = Player(50, 50, PLAYER_SIZE, False, PLAYER_1_CONTROLS)
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
        r += COLOUR_CHANGE_SPEED * round(game.time_scale, 2)
        b -= COLOUR_CHANGE_SPEED * round(game.time_scale, 2)
        if r >= COLOUR_BRIGHTNESS:
            r = COLOUR_BRIGHTNESS
            increasing_color = 1
    if increasing_color == 1:
        g += COLOUR_CHANGE_SPEED * round(game.time_scale, 2)
        r -= COLOUR_CHANGE_SPEED * round(game.time_scale, 2)
        if g >= COLOUR_BRIGHTNESS:
            g = COLOUR_BRIGHTNESS
            increasing_color = 2
    if increasing_color == 2:
        b += COLOUR_CHANGE_SPEED * round(game.time_scale, 2)
        g -= COLOUR_CHANGE_SPEED * round(game.time_scale, 2)
        if b >= COLOUR_BRIGHTNESS:
            b = COLOUR_BRIGHTNESS
            increasing_color = 0
    pressed = pygame.key.get_pressed()
    players.update(pressed)
    if pressed[pygame.K_SPACE]:
        game.time_scale = 0.5
        game.overlay_rect.width /= 1.2
        game.overlay_rect.height /= 1.2
        if game.overlay_alpha < 64:
            game.overlay_alpha *= 2
        screen.blit(
            game.overlay,
            (
                player.x + player.size / 2 - game.overlay_rect.width / 2,
                player.y + player.size / 2 - game.overlay_rect.height / 2
            )
        )
        if game.overlay_rect.width <= PLAYER_SIZE:
            game.reset_small_overlay()
    else:
        if game.overlay_rect.width >= OVERLAY_SIZE * 0.7:
            game.reset_overlay()
        else:
            game.slow(1)
            game.overlay_rect.width *= 1.2
            game.overlay_rect.height *= 1.2
            if game.overlay_alpha > 0:
                game.overlay_alpha /= 1.2
            screen.blit(
                game.overlay,
                (
                    player.x + player.size / 2 - game.overlay_rect.width / 2,
                    player.y + player.size / 2 - game.overlay_rect.height / 2
                )
            )
    enemies.update()
    game.update()
    trans_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    trans_overlay.set_alpha(50 * game.time_scale)
    trans_overlay.fill((
        limit(r + (250 - COLOUR_BRIGHTNESS) * game.time_scale ** 3, 0, 254),
        limit(g + (250 - COLOUR_BRIGHTNESS) * game.time_scale ** 3, 0, 254),
        limit(b + (250 - COLOUR_BRIGHTNESS) * game.time_scale ** 3, 0, 254),
        0
    ))
    screen.blit(trans_overlay, (0, 0))
    enemies.draw(screen)
    players.draw(screen)
    pygame.display.flip()
    clock.tick(60)