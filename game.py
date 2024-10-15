import random
import pygame
import time
import math
from constants import *
from maze import Maze
from pacman import Pacman
from ghost import Ghost

class Game:
    def __init__(self):
        self.maze = Maze()
        self.pacman = Pacman(CELL_SIZE * 1.5, CELL_SIZE * 1.5)
        self.ghosts = []
        for _ in range(NUM_GHOSTS):
            while True:
                x = random.randint(1, len(MAZE_LAYOUT[0]) - 2) * CELL_SIZE + CELL_SIZE // 2
                y = random.randint(1, len(MAZE_LAYOUT) - 2) * CELL_SIZE + CELL_SIZE // 2
                ghost_rect = pygame.Rect(x - 10, y - 10, 20, 20)
                if not any(ghost_rect.colliderect(wall) for wall in self.maze.walls):
                    self.ghosts.append(Ghost(x, y))
                    break
        self.score = 0
        self.power_mode = False
        self.power_mode_time = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and self.game_over:
                if event.key == pygame.K_SPACE:
                    self.reset_game()
        return True

    def update(self):
        if not self.game_over:
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                dx = -1
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = 1
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                dy = -1
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                dy = 1
            
            if dx != 0 or dy != 0:
                self.pacman.move(dx, dy, self.maze)
            
            for ghost in self.ghosts:
                ghost.move(self.maze)
            
            self.check_collisions()
            
            if self.power_mode and time.time() - self.power_mode_time > 5:
                self.power_mode = False
            
            self.check_ghost_collisions()

    def check_collisions(self):
        pacman_rect = pygame.Rect(self.pacman.x - self.pacman.radius, self.pacman.y - self.pacman.radius, 
                                  self.pacman.radius * 2, self.pacman.radius * 2)
        
        for dot in self.maze.dots[:]:
            if pacman_rect.collidepoint(dot['x'], dot['y']):
                self.maze.dots.remove(dot)
                self.score += 10
        
        for pellet in self.maze.power_pellets[:]:
            if pacman_rect.collidepoint(pellet['x'], pellet['y']):
                self.maze.power_pellets.remove(pellet)
                self.power_mode = True
                self.power_mode_time = time.time()
                self.score += 50
        
        for ghost in self.ghosts[:]:
            if pacman_rect.collidepoint(ghost.x, ghost.y):
                if self.power_mode:
                    self.ghosts.remove(ghost)
                    self.score += 200
                else:
                    self.game_over = True

    def draw(self, surface):
        surface.fill(BLACK)
        self.maze.draw(surface)
        self.pacman.draw(surface)
        for ghost in self.ghosts:
            ghost.draw(surface, self.power_mode)
        
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        surface.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press SPACE to restart", True, WHITE)
            surface.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2))

    def reset_game(self):
        self.__init__()

    def check_ghost_collisions(self):
        for i, ghost1 in enumerate(self.ghosts):
            for ghost2 in self.ghosts[i+1:]:
                if ((ghost1.x - ghost2.x)**2 + (ghost1.y - ghost2.y)**2)**0.5 < 20:
                    # If ghosts are too close, slightly adjust their positions
                    angle = random.uniform(0, 2 * math.pi)
                    ghost1.x += math.cos(angle) * 5
                    ghost1.y += math.sin(angle) * 5
                    ghost2.x -= math.cos(angle) * 5
                    ghost2.y -= math.sin(angle) * 5
