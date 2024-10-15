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
        directions = ['up', 'down', 'left', 'right']
        random.shuffle(directions)
        
        for direction in directions:
            new_x, new_y = self.x, self.y
            if direction == 'up':
                new_y -= self.speed
            elif direction == 'down':
                new_y += self.speed
            elif direction == 'left':
                new_x -= self.speed
            elif direction == 'right':
                new_x += self.speed
            
            ghost_rect = pygame.Rect(new_x - 10, new_y - 10, 20, 20)
            if not any(ghost_rect.colliderect(wall) for wall in maze.walls):
                self.x, self.y = new_x, new_y
                self.direction = direction
                break

    def draw(self, surface, power_mode):
        color = RED if not power_mode else BLUE
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 20)
