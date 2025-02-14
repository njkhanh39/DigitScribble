import pygame
from game import Game


pygame.init()

g = Game()

while g.running:
    g.game_loop()

pygame.quit()






