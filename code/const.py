from xml.dom.minidom import Entity

import pygame
from pygame.examples.grid import WINDOW_WIDTH

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (159, 197, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
Entity_SPEED = {
    'Level2': 0,
    'Level2.2':1,
    'Level2.3':2,
    'Level2.4':3,
    'Level2.5':4,
    'Player1':3,
    'Player2': 3,
    'Enemy1':2,
    'Enemy2': 1,
}

#





# M
MENU_OPTION = (
              'NEW GAME 1P,'
              'NEW GAME 2P - COOPERATIVE',
              'NEW GAME 2P - COMPETITIVE',
              'SCORE',
              'EXIT')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT =  {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

#S
SPAWN_TIME = 4000





# W
WIN_WIDTH = 576
WIN_HEIGHT: int = 324


