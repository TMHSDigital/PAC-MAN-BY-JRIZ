import pygame
from constants import *

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = PACMAN_RADIUS
        self.speed = PACMAN_SPEED

    def move(self, dx, dy, maze):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        
        pacman_rect = pygame.Rect(new_x - self.radius, new_y - self.radius, self.radius * 2, self.radius * 2)
        
        if not any(pacman_rect.colliderect(wall) for wall in maze.walls):
            self.x, self.y = new_x, new_y

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.radius)
