import pygame

# Pygame Initialization
pygame.init()

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        # Variables
        self.x = x
        self.y = y
        self.screen = screen
        self.color = (255, 0, 0)
        self.speed = 7
        self.player = pygame.Rect(x, y, 60, 60)
        self.player.center = (x, y)
        self.jump = False

    def move_right(self):
        # Moving right
        self.player.x += self.speed

        # Collision
        if self.player.right >= 750:
            self.player.right = 750

    def move_left(self):
        # Moving left
        self.player.x -= self.speed

        # Collision
        if self.player.left <= 0:
            self.player.left = 0

    def jumping(self, key):
        # Jumping
        if key[pygame.K_SPACE] and self.jump == False:
            self.jump = True

        if self.jump == True:
            self.player.y -= self.speed * 4
            self.speed -= 1
            if self.speed < -7:
                self.jump = False
                self.speed = 7

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.player)
