import pygame
from random import randint

# Pygame Initialization
pygame.init()

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, width, screen):
        pygame.sprite.Sprite.__init__(self)
        # Variables
        self.screen = screen
        self.x = randint(width // 2 - 350, width - 55)
        self.y = randint(340, 465)
        self.color = (202, 222, 1)
        self.coin = pygame.Rect(self.x, self.y, 7, 7)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.coin)
