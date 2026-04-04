import pygame
import sys
from constants import *
from init import *
from objects import *




clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top >= 5:
        player.y -= PADDEL_SPEED
    if keys[pygame.K_DOWN] and player.bottom <= HEIGHT - 5:
        player.y += PADDEL_SPEED

    game_display.fill((112, 146, 190))
    pygame.draw.rect(game_display, WHITE, player)
    pygame.draw.rect(game_display, WHITE, opponent)
    pygame.draw.line(game_display, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)
    pygame.display.update()
    clock.tick(60)






