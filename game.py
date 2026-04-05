import pygame
import sys
from constants import *
from init import *
from objects import *
from functions import show_score, update_player


clock = pygame.time.Clock()

player_score = 0
opponent_score = 0
collision = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player = update_player(player, keys)
    
    if ball.bottom >= HEIGHT or ball.top <= 0:
        ball_yd *= -1

    if (ball.colliderect(player) and not collision) or (ball.colliderect(opponent) and collision):
        ball_xd *= -1
        collision = not collision

    ball.x += ball_xd
    ball.y += ball_yd

    if ball.right > player.center[0]:
        opponent_score += 1
        ball.x, ball_y = WIDTH//2 - BALL_SIZE[0]//2, HEIGHT//2 - BALL_SIZE[1] //2
    elif ball.left < opponent.center[0]:
        player_score += 1
        ball.x, ball_y = WIDTH//2 - BALL_SIZE[0]//2, HEIGHT//2 - BALL_SIZE[1] //2

    if ball.center[1] > opponent.center[1] and opponent.bottom < HEIGHT:
        opponent.y += PADDEL_SPEED
    if ball.center[1] < opponent.center[1] and opponent.top > 0:
        opponent.y -= PADDEL_SPEED

    game_display.fill((112, 146, 190))
    show_score(game_display, str(opponent_score), WHITE, True)
    show_score(game_display, str(player_score), WHITE, False)
    pygame.draw.ellipse(game_display, WHITE, ball)
    pygame.draw.rect(game_display, WHITE, player)
    pygame.draw.rect(game_display, WHITE, opponent)
    pygame.draw.line(game_display, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)
    pygame.display.update()
    clock.tick(60)






