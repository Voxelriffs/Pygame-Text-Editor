import pygame
import sys

pygame.init()

# Window Setup
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Editor v0.0.1")
clock = pygame.time.Clock()

# Font & Colors
font = pygame.font.SysFont("consolas", 18)
BG = (40, 44, 52)

running = True
while running:

    # Handles All Input (EX: Text Input & Backspace)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    pygame.display.flip()

sys.exit()
pygame.QUIT