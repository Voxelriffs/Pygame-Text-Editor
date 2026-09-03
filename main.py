import pygame
import sys

pygame.init()

# Window Setup
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Editor v0.0.1")
clock = pygame.time.Clock()

# Font & Colors
MAIN_FONT = pygame.font.SysFont("consolas", 18)
BG_COLOR = (40, 44, 52)
TEXT_COLOR = (171, 178, 191)
LINE_NUMBER_COLOR = (123, 130, 140)
CURSOR_COLOR = (82, 139, 255)

#Editor Starting State
lines = ["# Welcome to my PyGame Text Editor!", ""]
cursor_row = 1
cursor_col = 0

running = True
while running:

    # Handles All Input (EX: Text Input & Backspace)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.TEXTINPUT:
            # Insert anything typed at current cursor position
            current_line = lines[cursor_row]
            lines[cursor_row] = current_line[:cursor_col] + event.text + current_line[cursor_col:]
            cursor_col += len(event.text)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if cursor_col > 0:
                    current_line = lines[cursor_row]
                    lines[cursor_row] = current_line[:cursor_col - 1] + current_line[cursor_col:]
                    cursor_col -= 1
                elif cursor_row > 0:
                    # Move to the end of the previous line
                    cursor_col = len(lines[cursor_row - 1])
                    lines[cursor_row - 1] += lines[cursor_row]
                    del lines[cursor_row]
                    cursor_row -= 1

            elif event.key == pygame.K_RETURN:
                current_line = lines[cursor_row]
                lines.insert(cursor_row + 1, current_line[cursor_col:])
                lines[cursor_row] = current_line[:cursor_col]
                cursor_row += 1
                cursor_col = 0

            elif event.key == pygame.K_LEFT and cursor_col > 0:
                cursor_col -= 1
            elif event.key == pygame.K_RIGHT and cursor_col < len(lines[cursor_row]):
                cursor_col += 1

    # Drawing
    screen.fill(BG_COLOR)

    char_width, char_height = MAIN_FONT.size(" ")
    margin_left = 60

    for i, line in enumerate(lines):
        # Draw line numbers
        num_surface = MAIN_FONT.render(str(i + 1).rjust(3), True, LINE_NUMBER_COLOR)
        screen.blit(num_surface, (10, i * char_height + 10))

        # Draw text
        text_surface = MAIN_FONT.render(line, True, TEXT_COLOR)
        screen.blit(text_surface, (margin_left, i * char_height + 10))

    # Draw cursor
    cursor_x = margin_left + (cursor_col * char_width)
    cursor_y = (cursor_row * char_height) + 10
    pygame.draw.rect(screen, CURSOR_COLOR, (cursor_x, cursor_y, 2, char_height))

    pygame.display.flip()
    clock.tick(60)

sys.exit()
pygame.QUIT