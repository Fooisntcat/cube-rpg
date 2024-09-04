#IMPORTS
import pygame
import sys
import os
import time

#CONFIG
WIDTH = 1920
HEIGHT = 1080
running = True
vel = 5
jumpvalue = 0

#jumping
clock = pygame.time.Clock()
y_gravity = 2
jump_h = 30
y_vel = jump_h

# Init
pygame.init()
info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h
win = pygame.display.set_mode((screen_width-10, screen_height-50))

# Display Setup
pygame.display.update()
pygame.display.set_caption("CubeRPG")

# COLOURS
WHITE = (255, 255, 255)
BLUE = (173, 216, 230)
BLACK = (0,0,0)
GREEN = (0,255,0)

# PLAYER VARIABLES
x_pos = 300
y_pos = 700
isJump = False

while running:
    clock.tick(60)
    win.fill((0, 0, 0),(0 , 0, screen_width, 750))
    rect1 = pygame.draw.rect(win, BLACK,(x_pos , y_pos, 50, 50)) 
    rect2 = pygame.draw.rect(win, BLUE, (0, 750, 1550, 100))
    rect3 = pygame.draw.rect(win, BLUE, (800, 600, 200, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x_pos > vel:
         x_pos -= vel
    if keys[pygame.K_RIGHT] and x_pos < screen_width - vel - 60:
        x_pos += vel
    if keys[pygame.K_SPACE]:
        isJump = True     
    if isJump:
        y_pos -= y_vel
        y_vel -= y_gravity
        if y_vel <- jump_h:
            isJump = False
            y_vel = jump_h
        if collide:
            y_vel = 0

    #collision
    collide = rect1.colliderect(rect3)
    collide2 = rect1.colliderect(rect2)

    if collide:
        rect1.bottom = rect3.top
        if rect1.top == rect3.bottom:
            y_pos = 700
            pygame.display.update()
    if collide2:
        y_pos = 700

pygame.quit

# OTHERS
