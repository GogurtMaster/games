import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake")


food_color = (255, 0, 0)
food_x = 400
food_y = 200
snake_color = (50, 205, 50)
snake = [(400, 400)]
snake_size = 20

speed = 0.12

score = 0
level = 1

running = True

direction = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_d] and direction != "LEFT":
        direction = "RIGHT"
    if keys[pygame.K_w] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_s] and direction != "UP":
        direction = "DOWN"

    head_x, head_y = snake[0]
    if direction == "LEFT":
        new_head = (head_x - snake_size, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + snake_size, head_y)
    elif direction == "UP":
        new_head = (head_x, head_y - snake_size)
    elif direction == "DOWN":
        new_head = (head_x, head_y + snake_size)
    else:
        new_head = (head_x, head_y)

    snake.insert(0, new_head)

    if new_head == (food_x, food_y) :
        food_x = random.randint(0,800 - snake_size) // 20 * 20
        food_y = random.randint(20,800 - snake_size) // 20 * 20
        score += 1
        while (food_x, food_y) in snake:
            food_x = random.randint(0, 800 - snake_size) // 20 * 20
            food_y = random.randint(20, 800 - snake_size) // 20 * 20
        if score % 20 == 0:
            speed -= .01
            level += 1
    else:
        snake.pop()

    if (
        new_head[0] < 0 or new_head[0] >= 800 or
        new_head[1] < 20 or new_head[1] >= 800 or
        new_head in snake[1:]
    ):
        direction = ""
        running = False


    for segment in snake:
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], snake_size, snake_size))
    pygame.draw.rect(screen, food_color, (food_x, food_y, snake_size, snake_size))

    pygame.draw.line(screen, (255, 255, 255), (0, 20), (800, 20), 2)

    font = pygame.font.SysFont(None, 20)
    score_text = font.render(f"score: {score}", True, (255, 255, 255))
    level_text = font.render(f"level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 5))
    screen.blit(level_text, (80, 5))

    time.sleep(speed)
    pygame.display.flip()   
    
pygame.quit()
sys.exit()