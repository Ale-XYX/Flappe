import pygame
import sys
import pip

sys.path.insert(0, './src')
import game

if __name__ == '__main__':
    pygame.init()
    game.title()
    pygame.quit()
