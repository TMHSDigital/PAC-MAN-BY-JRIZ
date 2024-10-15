import pygame
import traceback
from constants import *
from game import Game

def main():
    try:
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
    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
