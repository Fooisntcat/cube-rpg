import pygame
import sys
import os

WIDTH = 1920
HEIGHT = 1080

pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h

window_width,window_height = WIDTH-10,HEIGHT-500
win = pygame.display.set_mode((screen_width-10, screen_height-50))

pygame.display.update()

pygame.display.set_caption("CubeRPG")



BLOCK_SIZE = 260
cube_cord = [[WIDTH//4, HEIGHT//4]]
WHITE = (255, 255, 255)
cube = WHITE

running = True

while running:

    pygame.draw.rect(win, (255, 255, 255), (480, 360, BLOCK_SIZE, BLOCK_SIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

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
