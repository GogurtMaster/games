import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("ship shoot")


food_color = (255, 0, 0)
food_x = 300
food_y = 200
ship_color = (50, 205, 50)
ship_x = 300
ship_y = 580
ship_size = 20

speed = 0.15

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
    if keys[pygame.K_a] and ship_x != 0:
        ship_x -= .25
    if keys[pygame.K_d] and ship_x != 580:
        ship_x += .25
    

    pygame.draw.rect(screen, ship_color, (ship_x, ship_y, ship_size, ship_size))
    pygame.draw.rect(screen, food_color, (food_x, food_y, ship_size, ship_size))

    pygame.draw.line(screen, (255, 255, 255), (0, 20), (800, 20), 2)

    font = pygame.font.SysFont(None, 20)
    score_text = font.render(f"score: {score}", True, (255, 255, 255))
    level_text = font.render(f"level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 5))
    screen.blit(level_text, (80, 5))

    pygame.display.flip()   
    
pygame.quit()
sys.exit()