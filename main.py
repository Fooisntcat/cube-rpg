#IMPORTS
import pygame
import sys
import os
import time

#CONFIG
WIDTH = 1920
HEIGHT = 1080
running = True
vel = 3

info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h
win = pygame.display.set_mode((screen_width-10, screen_height-50))

# Init
pygame.init()

# Display Setup
pygame.display.update()
pygame.display.set_caption("CubeRPG")

# COLOURS
WHITE = (255, 255, 255)
BLUE = (173, 216, 230)

# PLAYER VARIABLES
x_pos = 300
y_pos = 300
isJump = False
jumpCount = 10

while running:
    pygame.draw.rect(win, BLUE, (0, 750, 1550, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x_pos > vel:
         x_pos -= vel
    if keys[pygame.K_RIGHT] and x_pos < screen_width - vel - 60:
        x_pos += vel
    if keys[pygame.K_UP] and y_pos > vel:
        y_pos -= vel
    if keys[pygame.K_DOWN] and y_pos < screen_height - vel - 160:
        y_pos += vel

    win.fill((0, 0, 0),(0 , 0, screen_width, 750))

    pygame.draw.rect(win,(180,180,180),(x_pos , y_pos, 50, 50)) 
    pygame.display.update()
    
pygame.quit

# OTHERS
"""
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        #starts new game
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
"""