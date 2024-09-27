import pygame
from pygame.locals import *
import create_board
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

window = pygame.display.set_mode((0, 0), pygame.RESIZABLE) # set to FULLSCREEN later

font = pygame.font.Font(None, 36)  # None sets default font, 36 is the font size
 
create_board.create_board(window)
coordinates = create_board.initialize_hex_positions()

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

    for number, coord in coordinates.items():
        # Render the text (convert number to string)
        text_surface = font.render(str(number), True, (0, 0, 0))  # Black color
        # Blit the text onto the screen at the given coordinates
        window.blit(text_surface, coord)

    # Update the display
    pygame.display.flip()