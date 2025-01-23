import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("ship shoot")

image = pygame.image.load("ufo.png").convert_alpha()
image = pygame.transform.scale(image, (40, 20))



food_color = (255, 0, 0)
food_x = 300
food_y = 200
ship_color = (50, 205, 50)
ship_x = 300
ship_y = 580
ship_size = 20

projectiles = []
projectile_width = 5
projectile_height = 20
projectile_speed = 1.3

projectile_active = False


score = 0
level = 0

running = True

direction = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
######################################################################################

    if keys[pygame.K_SPACE] and not projectile_active:
        projectile_x = ship_x + 40 // 2 - projectile_width // 2
        projectile_y = ship_y
        projectiles.append([projectile_x, projectile_y])
        projectile_active = True
#####################################################################################


    if keys[pygame.K_a]:
        if ship_x > 0:
            if keys[pygame.K_LSHIFT]:
                ship_x -= 0.4
            else:
                ship_x -= 0.25

    if keys[pygame.K_d]:
        if ship_x < 560:
            if keys[pygame.K_LSHIFT]:
                ship_x += 0.4
            else:
                ship_x += 0.25

###########################################################
    for projectile in projectiles:
        projectile[1] -= projectile_speed

    projectiles = [p for p in projectiles if p[1] > 0]
    if not projectiles:
        projectile_active = False
############################################################

    

    screen.blit(image, (ship_x, ship_y))
    pygame.draw.rect(screen, food_color, (food_x, food_y, ship_size, ship_size))

##############################################################################
    for projectile in projectiles:
        pygame.draw.rect(screen, (255, 0, 0), (projectile[0], projectile[1], projectile_width, projectile_height))
###############################################################################

    if projectile_y == food_y:
        game = 1

    pygame.draw.line(screen, (255, 255, 255), (0, 20), (800, 20), 2)

    font = pygame.font.SysFont(None, 20)
    score_text = font.render(f"score: {score}", True, (255, 255, 255))
    level_text = font.render(f"level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 5))
    screen.blit(level_text, (80, 5))

    pygame.display.flip()   
    
pygame.quit()
sys.exit()