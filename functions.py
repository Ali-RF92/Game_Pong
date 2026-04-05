import pygame
from init import game_display
from objects import FONT
from constants import *

def show_score(Surface, _str, color, which):
    str_obj = FONT.render(_str, True, color)
    position = list(str_obj.get_size())

    if which:
        position[0] = (WIDTH//2) - position[0] - 20
    else:
        position[0] = (WIDTH//2) + 20

    Surface.blit(str_obj, position)