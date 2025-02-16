# Importing products from outside this country will go through a hard and long procedure, since Beacukai is a piece of shit of a goverment agency. This chunk-of-a-code could be illegal though.
import pygame
import sys
import random

# Initialize that pygame library..? module..? Whatever.
pygame.init()

# I remember when Terry A Davis write TempleOS and God told him the operating system should be 640 x 480. I want to use that to my game, but, 800 x 600 already looks fine and big enough on my screen.
WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Clock to control the framerate.
clock = pygame.time.Clock()

# Load images/assets taken from a site. It's open domain asset so I will be fine.
try:
    player_img = pygame.image.load('player.png')
    bullet_img = pygame.image.load('bullet.png')
    enemy_img = pygame.image.load('enemy.png')
except pygame.error as e:
    print(f"Error loading images, you missing this asset retard: {e}")
    sys.exit()

print(f"Player image size: {player_img.get_size()}")
print(f"Bullet image size: {bullet_img.get_size()}")
print(f"Enemy image size: {enemy_img.get_size()}")

player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10
player_speed = 5

bullets = []

enemies = []

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    if keys[pygame.K_SPACE]:
        bullet = bullet_img.get_rect()
        bullet.centerx = player_rect.centerx
        bullet.bottom = player_rect.top
        bullets.append(bullet)

    for bullet in bullets:
        bullet.y -= 10
        screen.blit(bullet_img, bullet)
        print(f"Bullet position: {bullet.x}, {bullet.y}")

    bullets = [bullet for bullet in bullets if bullet.y > 0]

    if len(enemies) < 5:
        enemy = enemy_img.get_rect()
        enemy.x = random.randint(0, WIDTH - enemy.width)
        enemy.y = random.randint(-100, -50)
        enemies.append(enemy)

    for enemy in enemies:
        enemy.y += 3
        screen.blit(enemy_img, enemy)
        print(f"Enemy position: {enemy.x}, {enemy.y}")  # This is the part when almost got me into rage, because most of my debugging time are trying to solve why the heck the bullet and the enemy assets did not fucking appear on the screen.

    enemies = [enemy for enemy in enemies if enemy.y < HEIGHT]

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    for enemy in enemies:
        if enemy.y > HEIGHT:
            running = False

    screen.blit(player_img, player_rect)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # The fps / framerate is limit at 60.
    clock.tick(60)

pygame.quit()
sys.exit()

# I run through 20 minutes of trial and error, most are solved with huge help from AI. Is it unethical if I being desperate and letting AI to fix my code? It doesn't matter to me, as long as the shit works and works as intended.