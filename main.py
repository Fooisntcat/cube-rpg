import pygame
import sys

WIDTH = 640
HEIGHT = 880
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("CubeRPG")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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



BLOCK_SIZE = 260
cube_cord = [[WIDTH//4, HEIGHT//4]]
WHITE = (255, 255, 255)
while running:
    def draw_objects():
        win.fill((0, 0, 0))
        for cord in cube_cord:
            pygame.draw.rect(win, WHITE, pygame.Rect(cord[0], cord[1], BLOCK_SIZE, BLOCK_SIZE))

draw_objects()
pygame.display.update()

    #def update(self):
    
    #def draw(self):

    #def main(self):

    #def game_over(self):

    #def intro_screen(self):
