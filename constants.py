import pygame

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game settings
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 30
FPS = 60

# Pacman settings
PACMAN_SPEED = 5
PACMAN_RADIUS = 20

# Ghost settings
NUM_GHOSTS = 4
GHOST_SPEED = 3

# Maze layout
MAZE_LAYOUT = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X........X.........X",
    "X.XX.XXX.X.XXX.XX..X",
    "X.................PX",
    "X.XX.X.XXXXX.X.XX..X",
    "X....X...X...X.....X",
    "XXXX.XXX.X.XXX.XXXXX",
    "   X.X.........X   ",
    "XXXX.X.XXX-XXX.XXXXX",
    "....P...X   X.......",
    "XXXX.X.XXXXX.X.XXXXX",
    "   X.X.........X   ",
    "XXXX.X.XXXXX.X.XXXXX",
    "X........X.........X",
    "X.XX.XXX.X.XXX.XX..X",
    "X..X...........X..PX",
    "XX.X.X.XXXXX.X.X.XXX",
    "X....X...X...X.....X",
    "X.XXXXXX.X.XXXXXX..X",
    "X.................PX",
    "XXXXXXXXXXXXXXXXXXXX"
]
