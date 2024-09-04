import pygame
import sys
import os
import time

WIDTH = 1920
HEIGHT = 1080
x = 300
y = 300

pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h
win = pygame.display.set_mode((screen_width-10, screen_height-50))

pygame.display.update()

pygame.display.set_caption("CubeRPG")



BLOCK_SIZE = 260
cube_cord = [[WIDTH//4, HEIGHT//4]]
WHITE = (255, 255, 255)
cube = WHITE

running = True
vel = 3

w=40
h=60

while running:

    pygame.draw.rect(win, (255, 255, 255), (0, 750, 1550, 100))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
         x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - vel - 60:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < screen_height - vel - 160:
        y += vel

    win.fill((0, 0, 0),(0 , 0, screen_width, 750))
    pygame.draw.rect(win,(180,180,180),(x , y, 50, 50)) 
    pygame.display.update()
    


    
pygame.quit

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


    #def update(self):
    
    #def draw(self):

    #def main(self):

    #def game_over(self):

    #def intro_screen(self):
