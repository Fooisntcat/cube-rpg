import pygame
from sprites import *
from config import *
import sys

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        #starts new game
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player = Player()

BLOCK_SIZE = 20
cube_cord = [[WIDTH//4, HEIGHT//4]]
def draw_objects():
    win.fill((0, 0, 0))
    for cord in cube_cord:
        pygame.draw.rect(win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    #def update(self):
    
    #def draw(self):

    #def main(self):

    #def game_over(self):

    #def intro_screen(self):
