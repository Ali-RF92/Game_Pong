import pygame
import sys
from constants import *
from init import *

player   = pygame.Rect(20, HEIGHT//2 - P_HEIGHT//2, P_WIDTH, P_HEIGHT)
opponent = pygame.Rect(WIDTH - 20 - P_WIDTH, HEIGHT//2 - P_HEIGHT//2, P_WIDTH, P_HEIGHT)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_display.fill((112, 146, 190))
    pygame.draw.rect(game_display, WHITE, player)
    pygame.draw.rect(game_display, WHITE, opponent)
    pygame.draw.line(game_display, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)
    pygame.display.update()







