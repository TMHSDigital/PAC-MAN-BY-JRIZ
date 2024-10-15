import pygame
from constants import *
from game import Game

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Enhanced Pacman")
    clock = pygame.time.Clock()
    
    game = Game()
    
    running = True
    while running:
        running = game.handle_events()
        game.update()
        game.draw(window)
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
