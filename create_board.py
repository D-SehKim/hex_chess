import pygame
from math import cos, sin, pi
from pygame.locals import *

def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
        for i in range(n)
    ], width)

def create_board(game_window):
    bg = pygame.image.load("assets/hex-6x6x6.png")
    #INSIDE OF THE GAME LOOP
    game_window.blit(bg, (0, 0))

def main():
    return None

if __name__ == "__main__":
    main()
