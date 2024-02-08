# Imports
import pygame
import player_system
import coin_system
import text_system

# Pygame Initialization
pygame.init()

# Screen
W = 750
H = 750
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Coin Collector by @AM2012")

# Clock
clock = pygame.time.Clock()
fps = 60

# Score
score = 0

# Font
font = pygame.font.SysFont("Agency FB", 30)

# Player
player = player_system.Player(W / 2, H / 2 + 90, screen)

# Coins
coins = []
for _ in range(10):
    coins.append(coin_system.Coin(W, screen))

# Run loop
run = True
while run:
    # BG
    screen.fill((36, 195, 232))

    # Drawing Ground
    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(W - 750, H / 2 + 60 + 60, 750, 255))

    # CLock
    clock.tick(fps)

    # Display Score
    text_system.draw_text(f"Score: {score}", font, W - 750, H / 2 - 375, screen)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Key detection
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            player.move_right()
        if key[pygame.K_a]:
            player.move_left()
        if key[pygame.K_r] and score == 10:
            score = 0
            for _ in range(10):
                coins.append(coin_system.Coin(W, screen))

    # Drawing player
    player.draw()

    # Jump
    player.jumping(key)

    # Drawing coins
    for coin in coins:
        coin.draw()

    # Check for collisions
    for coin in coins:
        if player.player.colliderect(coin.coin):
            score += 1
            coins.remove(coin)

    # Check if all the coins are collected
    if score == 10:
        text_system.draw_text("Game Over!You have collected all the 10 coins!", font, W - 600, H / 2, screen)
        text_system.draw_text("Press the 'r' key to restart the game", font, W / 2 - 175, H / 2 + 275, screen)

    # Updating
    pygame.display.flip()

pygame.quit()
