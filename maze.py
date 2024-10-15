import pygame
from constants import *

class Maze:
    def __init__(self):
        self.walls = []
        self.dots = []
        self.power_pellets = []
        self.generate_maze()

    def generate_maze(self):
        for y, row in enumerate(MAZE_LAYOUT):
            for x, cell in enumerate(row):
                if cell == 'X':
                    self.walls.append(pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif cell == '.':
                    self.dots.append({'x': x * CELL_SIZE + CELL_SIZE // 2, 'y': y * CELL_SIZE + CELL_SIZE // 2, 'radius': 3})
                elif cell == 'P':
                    self.power_pellets.append({'x': x * CELL_SIZE + CELL_SIZE // 2, 'y': y * CELL_SIZE + CELL_SIZE // 2, 'radius': 8})

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, BLUE, wall)
        for dot in self.dots:
            pygame.draw.circle(surface, WHITE, (int(dot['x']), int(dot['y'])), dot['radius'])
        for pellet in self.power_pellets:
            pygame.draw.circle(surface, WHITE, (int(pellet['x']), int(pellet['y'])), pellet['radius'])
