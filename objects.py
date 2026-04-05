import pygame
from constants import *


opponent   = pygame.Rect(20, HEIGHT//2 - P_HEIGHT//2, P_WIDTH, P_HEIGHT)
player = pygame.Rect(WIDTH - 20 - P_WIDTH, HEIGHT//2 - P_HEIGHT//2, P_WIDTH, P_HEIGHT)

FONT = pygame.font.Font(None, 36)

ball = pygame.Rect(WIDTH//2 - BALL_SIZE[0]//2, HEIGHT//2 - BALL_SIZE[1] //2, BALL_SIZE[0], BALL_SIZE[1])
ball_xd = BALL_SPEED
ball_yd = BALL_SPEED