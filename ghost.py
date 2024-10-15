import pygame
import random
from constants import *

class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = GHOST_SPEED
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def move(self, maze):
        if random.random() < 0.02:  # 2% chance to change direction
            self.direction = random.choice(['up', 'down', 'left', 'right'])
        
        new_x, new_y = self.x, self.y
        if self.direction == 'up':
            new_y -= self.speed
        elif self.direction == 'down':
            new_y += self.speed
        elif self.direction == 'left':
            new_x -= self.speed
        elif self.direction == 'right':
            new_x += self.speed
        
        ghost_rect = pygame.Rect(new_x - 20, new_y - 20, 40, 40)
        if not any(ghost_rect.colliderect(wall) for wall in maze.walls):
            self.x, self.y = new_x, new_y
        else:
            self.direction = random.choice(['up', 'down', 'left', 'right'])

    def draw(self, surface, power_mode):
        color = RED if not power_mode else BLUE
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 20)
