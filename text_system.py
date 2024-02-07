import pygame

# Pygame Initialization
pygame.init()

# Draw Text
def draw_text(text, font, x, y, screen):
    img = font.render(text, True, (53, 53, 53))
    screen.blit(img, (x, y))
