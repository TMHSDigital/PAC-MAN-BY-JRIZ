import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pacman")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Pacman
pacman_radius = 20
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_speed = 5

# Ghosts
num_ghosts = 4
ghosts = []
for _ in range(num_ghosts):
    ghost = {
        'x': random.randint(0, WIDTH),
        'y': random.randint(0, HEIGHT),
        'speed': 3
    }
    ghosts.append(ghost)

# Dots
num_dots = 50
dots = []
for _ in range(num_dots):
    dot = {
        'x': random.randint(0, WIDTH),
        'y': random.randint(0, HEIGHT),
        'radius': 5
    }
    dots.append(dot)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Pacman
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Keep Pacman within the screen
    pacman_x = max(pacman_radius, min(pacman_x, WIDTH - pacman_radius))
    pacman_y = max(pacman_radius, min(pacman_y, HEIGHT - pacman_radius))

    # Move ghosts
    for ghost in ghosts:
        if ghost['x'] < pacman_x:
            ghost['x'] += ghost['speed']
        elif ghost['x'] > pacman_x:
            ghost['x'] -= ghost['speed']
        if ghost['y'] < pacman_y:
            ghost['y'] += ghost['speed']
        elif ghost['y'] > pacman_y:
            ghost['y'] -= ghost['speed']

    # Check for collisions with dots
    for dot in dots[:]:
        if ((pacman_x - dot['x'])**2 + (pacman_y - dot['y'])**2)**0.5 < pacman_radius + dot['radius']:
            dots.remove(dot)
            score += 10

    # Check for collisions with ghosts
    for ghost in ghosts:
        if ((pacman_x - ghost['x'])**2 + (pacman_y - ghost['y'])**2)**0.5 < pacman_radius + 20:
            running = False

    # Clear the screen
    window.fill(BLACK)

    # Draw Pacman
    pygame.draw.circle(window, YELLOW, (pacman_x, pacman_y), pacman_radius)

    # Draw ghosts
    for ghost in ghosts:
        pygame.draw.circle(window, BLUE, (int(ghost['x']), int(ghost['y'])), 20)

    # Draw dots
    for dot in dots:
        pygame.draw.circle(window, WHITE, (dot['x'], dot['y']), dot['radius'])

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
