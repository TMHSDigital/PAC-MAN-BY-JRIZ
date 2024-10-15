import random
import pygame
import time
from constants import *
from maze import Maze
from pacman import Pacman
from ghost import Ghost

class Game:
    def __init__(self):
        self.maze = Maze()
        self.pacman = Pacman(CELL_SIZE * 1.5, CELL_SIZE * 1.5)
        self.ghosts = [Ghost(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_GHOSTS)]
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
            
            self.pacman.move(dx, dy, self.maze)
            
            for ghost in self.ghosts:
                ghost.move(self.maze)
            
            self.check_collisions()
            
            if self.power_mode and time.time() - self.power_mode_time > 5:
                self.power_mode = False

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
