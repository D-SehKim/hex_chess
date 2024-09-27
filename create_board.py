import pygame
from math import cos, sin, pi
from pygame.locals import *

VERTICAL = (0, 80)
DIAGONAL = (70, 40)
MIDDLE = (950, 540)
ROWS, COLS = 12, 12     # dimensions of the hex grid


def create_board(game_window):
    bg = pygame.image.load("assets/hex-6x6x6.png")
    #INSIDE OF THE GAME LOOP
    game_window.blit(bg, (550, 100))


hex_positions = {}

# Function to initialize hex positions and ranks
def initialize_hex_positions():
    valid_files = {
        'a': range(1, 6),   # a1 to a6
        'b': range(1, 7),   # b1 to b7
        'c': range(1, 8),   # c1 to c8
        'd': range(1, 9),  # d1 to d9
        'e': range(1, 10),  # e1 to e10
        'f': range(1, 11),  # f1 to f11
        'g': range(1, 10),  # g1 to g10
        'h': range(1, 9),  # h1 to h9
        'i': range(1, 8),   # i1 to i8
        'j': range(1, 7),   # j1 to j7
        'k': range(1, 6)    # k1 to k6
    }

    # Dictionary to store coordinates
    coordinates = {}

    return coordinates


def main():
    coordinates = initialize_hex_positions()
    print(coordinates)

if __name__ == "__main__":
    main()
