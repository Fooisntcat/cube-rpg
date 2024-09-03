# Example file showing a circle moving on screen
import os
import math
import random
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Cube RPG")
# pygame setup
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
dt = 0
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name):
     image = pygame.image.load(join("assets", "Background", name))
     _, _, width, height = image.get.rect()
     tiles = []

     for i in range(WIDTH// width + 1):
          for j in range (HEIGHT // height + 1):
               pos = [i * width, j * height]


def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    break
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
