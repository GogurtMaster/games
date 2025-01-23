import pygame
import sys
# import time
# import random
from pygame.locals import *

"""
Space Invader-like game for handheld game project
Controls:
Space: fire projectile
A: move left
D: move right
Left Shift + A: move left fast
Left Shift + D: move right fast
"""

# Variables controlling enemy attributes
enemy_color = (255, 0, 0)
enemy_x = 300
enemy_y = 200

# Variables controlling player attributes
ship_color = (50, 205, 50)
ship_x = 300
ship_y = 580
ship_size = 20

# Variables controlling projectile creation and attributes
projectiles = []
projectile_width = 5
projectile_height = 20
projectile_speed = 1.3
projectile_active = False

# Variables controlling score and level
score = 0
level = 0

running = True
direction = ""

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Ship Shoot")

# Load game assets
image = pygame.image.load("ufo.png").convert_alpha()

# Resize assets
image = pygame.transform.scale(image, (40, 20))

while running:
    # For loop checking if the player wants to exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    # Check if the player has pressed space to fire a projectile
    if keys[pygame.K_SPACE] and not projectile_active:
        projectile_x = ship_x + 40 // 2 - projectile_width // 2
        projectile_y = ship_y
        projectiles.append([projectile_x, projectile_y])  # Fixed: Append to the projectiles list
        projectile_active = True

    # Check if the player is trying to move the ship left or right
    if keys[pygame.K_a] and ship_x > 0:
        if keys[pygame.K_LSHIFT]:
            ship_x -= 0.4
        else:
            ship_x -= 0.25

    if keys[pygame.K_d] and ship_x < 560:
        if keys[pygame.K_LSHIFT]:
            ship_x += 0.4
        else:
            ship_x += 0.25

    # Move projectiles
    for p in projectiles:
        p[1] -= projectile_speed  # Fixed: Update the projectile's Y position

    # Remove projectiles that go off-screen
    projectiles = [p for p in projectiles if p[1] > 0]  # Fixed: Operate on the projectiles list

    # Check if projectiles exist
    if not projectiles:
        projectile_active = False

    # Draw the ship
    screen.blit(image, (ship_x, ship_y))
    pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, ship_size, ship_size))

    # Draw projectiles
    for p in projectiles:
        pygame.draw.rect(screen, (255, 0, 0), (p[0], p[1], projectile_width, projectile_height))

    # Draw UI elements
    pygame.draw.line(screen, (255, 255, 255), (0, 20), (800, 20), 2)
    font = pygame.font.SysFont(None, 20)
    score_text = font.render(f"score: {score}", True, (255, 255, 255))
    level_text = font.render(f"level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 5))
    screen.blit(level_text, (80, 5))

    pygame.display.flip()

pygame.quit()
sys.exit()
