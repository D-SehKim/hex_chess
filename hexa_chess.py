import pygame
from math import cos, sin, pi
from pygame.locals import *
import create_board
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((0, 0), pygame.RESIZABLE) # set to FULLSCREEN later
 
create_board.create_board(window)

# Draws the surface object to the screen.
pygame.display.update()

# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False