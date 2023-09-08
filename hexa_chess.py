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

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((0, 0), pygame.RESIZABLE) # set to FULLSCREEN later
 
# Fill the scree with white color
window.fill((255, 255, 255))

# THE CODE LOOKS UGLY BUT IT WORKS...
# making the entire board
middle = (725, 388)
MOVE_Y_FOR_FULL_UP = 70
MOVE_X_FOR_FULL_SIDE = 124
HALF_X = 62
HALF_Y = 35
HEX_SIZE = 40
AH = 50
EH = 110
negative_numbers = range(-1, -1000, -1)
positive_numbers = range(1, 1000, 1)

num_of_hex = [6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6]
start_x = 400
start_y = 213
color_list = ['gold', (255, 75, 0), 'orange']
position_list = []
edge_detection = []
rect_list = []
count = 0

for num in num_of_hex:
    if count < 5:
        for x in range(num):
            draw_regular_polygon(window, color_list[x%3], 6, HEX_SIZE, [start_x, start_y], width=0)
            position_list.append((start_x, start_y))
            rect_list.append(Rect((start_x, start_y), (35, 35)))
            start_y = start_y + MOVE_Y_FOR_FULL_UP

        start_x = start_x + HALF_X
        start_y = start_y - HALF_Y - (MOVE_Y_FOR_FULL_UP * num)

        color_list.append(color_list.pop(0))
    else:
        for x in range(num):
            draw_regular_polygon(window, color_list[x%3], 6, HEX_SIZE, [start_x, start_y], width=0)
            position_list.append((start_x, start_y))
            rect_list.append(Rect((start_x, start_y), (35, 35)))
            start_y = start_y + MOVE_Y_FOR_FULL_UP

        start_x = start_x + HALF_X
        start_y = start_y - HALF_Y - (MOVE_Y_FOR_FULL_UP * (num - 1))

        color_list = color_list[-1:] + color_list[:-1]
    count+=1

my_font = pygame.font.SysFont('Comic Sans MS', 14)
'''
for x in position_list:
    text_surface = my_font.render(f"{x}", False, (0, 0, 0))
    window.blit(text_surface, x)
'''

class Piece():
    def __init__(self, color, start_pos, name):
        self.color = color
        self.start_pos = start_pos
        self.current_pos = start_pos
        self.name = name

    def __str__(self):
        return f"{self.color} , {self.start_pos}"
    
    def update_current_pos(self, new_current_pos):
        self.current_pos = new_current_pos

    def move(self, cur_pos, new_pos, piece):
        self.coords = Rect(new_pos, (55, 55))
        self.update_current_pos(new_pos)

        cur_col = list(cur_pos)
        cur_col = [x - 21 for x in cur_col]
        color = window.get_at(tuple(cur_col))
        
        draw_regular_polygon(window, color, 6, HEX_SIZE, list(cur_pos), width=0)

        color = self.color

        imp = pygame.image.load(f"assets/{color}_{piece}.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))

        new_pos_sprite = [x - 27 for x in new_pos]
        tuple(new_pos_sprite)
        window.blit(self.image, new_pos_sprite)

    def hide_legal_moves(self, legal_moves):
        for moves in legal_moves:
            cur_col = list(moves)
            cur_col = [x - 21 for x in cur_col]
            color = window.get_at(tuple(cur_col))

            draw_regular_polygon(window, color, 6, HEX_SIZE, list(moves), width=0)

    def collide_detect(self, legal_moves, current_pos, color):
        collides = []
        for moves in legal_moves:
            if (moves[0], moves[1]) == (current_pos[0], current_pos[1]) and self.color == color:
                legal_moves.remove(moves)
                collides.append(moves)
            if (moves[0], moves[1]) == (current_pos[0], current_pos[1]) and self.color != color:
                collides.append(moves)
        legal_moves.append((self.current_pos[0], self.current_pos[1]))
        return legal_moves, collides

    def final_draw(self):
        imp = pygame.image.load(f"assets/{self.color}_{self.name}.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
        new_pos_sprite = self.current_pos

        new_pos_sprite = [x - 27 for x in new_pos_sprite]
        tuple(new_pos_sprite)
        window.blit(self.image, new_pos_sprite)

    def show_legal_moves(self, legal_moves):
        for moves in legal_moves:
            draw_regular_polygon(window, (255,255,255), 100, 7, list(moves), width=0)

class Pawn(Piece):
    def __init__(self, color, start_pos, name):
        super().__init__(color, start_pos, name)
        self.pawn_up = 'pawn'
        
        # creating sprites
        imp = pygame.image.load(f"assets/{color}_pawn.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))

        start_pos_sprite = [x - 27 for x in start_pos]
        tuple(start_pos_sprite)
        window.blit(self.image, start_pos_sprite)

        self.coords = Rect(start_pos_sprite, (55, 55))

    def __str__(self):
        return f"{self.color} Pawn, {self.start_pos}"

    def change_to_queen(self):
        self.pawn_up = 'queen'

        cur_col = list(self.current_pos)
        cur_col = [x - 21 for x in cur_col]
        color = window.get_at(tuple(cur_col))
        draw_regular_polygon(window, color, 6, HEX_SIZE, list(self.current_pos), width=0)

        imp = pygame.image.load(f"assets/{self.color}_queen.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
        current_position = self.current_pos.copy()
        current_position = [x - 27 for x in current_position]
        window.blit(self.image, current_position)

        pygame.draw.rect(window, 'white', (10, 10, 200, 200))
        self.qu = Rect((AH, AH), (0, 0))
        self.kn = Rect((EH, EH), (0, 0))
        self.ro = Rect((AH, EH), (0, 0))
        self.bi = Rect((EH, AH), (0, 0))

    def change_to_knight(self):
        self.pawn_up = 'knight'

        cur_col = list(self.current_pos)
        cur_col = [x - 21 for x in cur_col]
        color = window.get_at(tuple(cur_col))
        draw_regular_polygon(window, color, 6, HEX_SIZE, list(self.current_pos), width=0)

        imp = pygame.image.load(f"assets/{self.color}_knight.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
        current_position = self.current_pos.copy()
        current_position = [x - 27 for x in current_position]
        window.blit(self.image, current_position)

        pygame.draw.rect(window, 'white', (10, 10, 200, 200))
        self.qu = Rect((AH, AH), (0, 0))
        self.kn = Rect((EH, EH), (0, 0))
        self.ro = Rect((AH, EH), (0, 0))
        self.bi = Rect((EH, AH), (0, 0))

    def change_to_rook(self):
        self.pawn_up = 'rook'

        cur_col = list(self.current_pos)
        cur_col = [x - 21 for x in cur_col]
        color = window.get_at(tuple(cur_col))
        draw_regular_polygon(window, color, 6, HEX_SIZE, list(self.current_pos), width=0)

        imp = pygame.image.load(f"assets/{self.color}_rook.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
        current_position = self.current_pos.copy()
        current_position = [x - 27 for x in current_position]
        window.blit(self.image, current_position)

        pygame.draw.rect(window, 'white', (10, 10, 200, 200))
        self.qu = Rect((AH, AH), (0, 0))
        self.kn = Rect((EH, EH), (0, 0))
        self.ro = Rect((AH, EH), (0, 0))
        self.bi = Rect((EH, AH), (0, 0))

    def change_to_bishop(self):
        self.pawn_up = 'bishop'

        cur_col = list(self.current_pos)
        cur_col = [x - 21 for x in cur_col]
        color = window.get_at(tuple(cur_col))
        draw_regular_polygon(window, color, 6, HEX_SIZE, list(self.current_pos), width=0)

        imp = pygame.image.load(f"assets/{self.color}_bishop.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
        current_position = self.current_pos.copy()
        current_position = [x - 27 for x in current_position]
        window.blit(self.image, current_position)

        pygame.draw.rect(window, 'white', (10, 10, 200, 200))
        self.qu = Rect((AH, AH), (0, 0))
        self.kn = Rect((EH, EH), (0, 0))
        self.ro = Rect((AH, EH), (0, 0))
        self.bi = Rect((EH, AH), (0, 0))
    
    def upgrade_buttons(self):
        text_surface = my_font.render(f"Choose One", False, (0, 0, 0))
        window.blit(text_surface, (20, 20))

        self.qu = Rect((AH, AH), (50, 50))
        self.kn = Rect((EH, EH), (50, 50))
        self.ro = Rect((AH, EH), (50, 50))
        self.bi = Rect((EH, AH), (50, 50))

        pygame.draw.rect(window, 'grey', (AH, AH, 50, 50))
        pygame.draw.rect(window, 'grey', (EH, EH, 50, 50))
        pygame.draw.rect(window, 'grey', (AH, EH, 50, 50))
        pygame.draw.rect(window, 'grey', (EH, AH, 50, 50))

        imp = pygame.image.load(f"assets/{self.color}_queen.png").convert_alpha()
        im_qu = pygame.transform.scale(imp, (50, 50))
        window.blit(im_qu, (AH, AH))

        imp = pygame.image.load(f"assets/{self.color}_knight.png").convert_alpha()
        im_kn = pygame.transform.scale(imp, (50, 50))
        window.blit(im_kn, (EH, EH))

        imp = pygame.image.load(f"assets/{self.color}_rook.png").convert_alpha()
        im_ro = pygame.transform.scale(imp, (50, 50))
        window.blit(im_ro, (AH, EH))

        imp = pygame.image.load(f"assets/{self.color}_bishop.png").convert_alpha()
        im_bi = pygame.transform.scale(imp, (50, 50))
        window.blit(im_bi, (EH, AH))

    def check_legal_move(self, current_pos):
        legal_moves = []
        legal_moves.append((current_pos[0], current_pos[1])) 
        if [current_pos[0], current_pos[1]] == [self.start_pos[0], self.start_pos[1]]:
            legal_moves.append((current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP))
            legal_moves.append((current_pos[0], current_pos[1] - (MOVE_Y_FOR_FULL_UP * 2)))
        else:
            legal_moves.append((current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP))
        
        legal_moves.append(current_pos)

        if current_pos in edge_detection:
            self.upgrade()
        return legal_moves
  
class King(Piece):
    def __init__(self, color, start_pos, name):
        super().__init__(color, start_pos, name)

        # creating sprites
        imp = pygame.image.load(f"assets/{color}_king.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
    
        start_pos_sprite = [x - 27 for x in start_pos]
        tuple(start_pos_sprite)
        window.blit(self.image, start_pos_sprite)

        self.coords = Rect(start_pos_sprite, (55, 55))
    
    def __str__(self):
        return f"{self.color} King, {self.start_pos}"

    def check_legal_move(self, current_pos):
        legal_moves = []

        legal_moves.append((current_pos[0], current_pos[1]))        
        # THIS IS MOVING IN TOUCHING HEXAGONS
        if (current_pos[0], current_pos[1] + MOVE_Y_FOR_FULL_UP) in position_list:
            legal_moves.append((current_pos[0], current_pos[1] + MOVE_Y_FOR_FULL_UP))
        if (current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP) in position_list:
            legal_moves.append((current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP))     
        if (current_pos[0] + HALF_X, current_pos[1] + HALF_Y) in position_list:
            legal_moves.append((current_pos[0] + HALF_X, current_pos[1] + HALF_Y))
        if (current_pos[0] - HALF_X, current_pos[1] + HALF_Y) in position_list:
            legal_moves.append((current_pos[0] - HALF_X, current_pos[1] + HALF_Y))
        if (current_pos[0] + HALF_X, current_pos[1] - HALF_Y) in position_list:
            legal_moves.append((current_pos[0] + HALF_X, current_pos[1] - HALF_Y))
        if (current_pos[0] - HALF_X, current_pos[1] - HALF_Y) in position_list:
            legal_moves.append((current_pos[0] - HALF_X, current_pos[1] - HALF_Y))

        # STEAL THIS FOR BISHOP MOVEMENT
        if (current_pos[0] + MOVE_X_FOR_FULL_SIDE, current_pos[1]) in position_list:
            legal_moves.append((current_pos[0] + MOVE_X_FOR_FULL_SIDE, current_pos[1]))    
        if (current_pos[0] - MOVE_X_FOR_FULL_SIDE, current_pos[1]) in position_list:
            legal_moves.append((current_pos[0] - MOVE_X_FOR_FULL_SIDE, current_pos[1]))  
        if (current_pos[0] + HALF_X, current_pos[1] + MOVE_Y_FOR_FULL_UP + HALF_Y) in position_list:
            legal_moves.append((current_pos[0] + HALF_X, current_pos[1] + MOVE_Y_FOR_FULL_UP + HALF_Y))
        if (current_pos[0] + HALF_X, current_pos[1] - MOVE_Y_FOR_FULL_UP - HALF_Y) in position_list:
            legal_moves.append((current_pos[0] + HALF_X, current_pos[1] - MOVE_Y_FOR_FULL_UP - HALF_Y))
        if (current_pos[0] - HALF_X, current_pos[1] + MOVE_Y_FOR_FULL_UP + HALF_Y) in position_list:
            legal_moves.append((current_pos[0] - HALF_X, current_pos[1] + MOVE_Y_FOR_FULL_UP + HALF_Y))
        if (current_pos[0] - HALF_X, current_pos[1] - MOVE_Y_FOR_FULL_UP - HALF_Y) in position_list:
            legal_moves.append((current_pos[0] - HALF_X, current_pos[1] - MOVE_Y_FOR_FULL_UP - HALF_Y))

        return legal_moves

class Rook(Piece):
    def __init__(self, color, start_pos, name):
        super().__init__(color, start_pos, name)

        # creating sprites
        imp = pygame.image.load(f"assets/{color}_rook.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
    
        start_pos_sprite = [x - 27 for x in start_pos]
        tuple(start_pos_sprite)
        window.blit(self.image, start_pos_sprite)

        self.coords = Rect(start_pos_sprite, (55, 55))
    
    def __str__(self):
        return f"{self.color} Rook, {self.start_pos}"
    
    def check_legal_move(self, current_pos):
        legal_moves = []
        legal_moves.append((current_pos[0], current_pos[1]))        
        # THIS IS MOVING IN TOUCHING HEXAGONS
        # moving up and down is allowed?
        for num in range(10):
            numb = num + 1
            if (current_pos[0], current_pos[1] + MOVE_Y_FOR_FULL_UP * numb) in position_list:
                legal_moves.append((current_pos[0], current_pos[1] + MOVE_Y_FOR_FULL_UP * numb))

            if (current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP * numb) in position_list:
                legal_moves.append((current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP * numb))     

            if (current_pos[0] + HALF_X * numb, current_pos[1] + HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] + HALF_Y * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] + HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] + HALF_Y * numb))

            if (current_pos[0] + HALF_X * numb, current_pos[1] - HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] - HALF_Y * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] - HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] - HALF_Y * numb))

        return legal_moves

class Bishop(Piece):
    def __init__(self, color, start_pos, name):
        super().__init__(color, start_pos, name)

        # creating sprites
        imp = pygame.image.load(f"assets/{color}_bishop.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
    
        start_pos_sprite = [x - 27 for x in start_pos]
        tuple(start_pos_sprite)
        window.blit(self.image, start_pos_sprite)

        self.coords = Rect(start_pos_sprite, (55, 55))
    
    def __str__(self):
        return f"{self.color} Bishop, {self.start_pos}"
    
    def check_legal_move(self, current_pos):
        legal_moves = []
        legal_moves.append((current_pos[0], current_pos[1]))        
        # THIS IS MOVING IN TOUCHING HEXAGONS
        # moving up and down is allowed?
        for num in range(10):
            numb = num + 1
            if (current_pos[0] + MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]) in position_list:
                legal_moves.append((current_pos[0] + MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]))    

            if (current_pos[0] - MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]) in position_list:
                legal_moves.append((current_pos[0] - MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]))  

            if (current_pos[0] + HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))
            
            if (current_pos[0] + HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))

        return legal_moves

class Queen(Piece):
    def __init__(self, color, start_pos, name):
        super().__init__(color, start_pos, name)

        # creating sprites
        imp = pygame.image.load(f"assets/{color}_Queen.png").convert_alpha()
        self.image = pygame.transform.scale(imp, (55, 55))
    
        start_pos_sprite = [x - 27 for x in start_pos]
        tuple(start_pos_sprite)
        window.blit(self.image, start_pos_sprite)

        self.coords = Rect(start_pos_sprite, (55, 55))
    
    def __str__(self):
        return f"{self.color} Queen, {self.current_pos}"
    
    def check_legal_move(self, current_pos):
        legal_moves = []
        legal_moves.append((current_pos[0], current_pos[1]))        
        # THIS IS MOVING IN TOUCHING HEXAGONS
        # moving up and down is allowed?
        for num in range(10):
            numb = num + 1
            if (current_pos[0] + MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]) in position_list:
                legal_moves.append((current_pos[0] + MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]))    

            if (current_pos[0] - MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]) in position_list:
                legal_moves.append((current_pos[0] - MOVE_X_FOR_FULL_SIDE * numb, current_pos[1]))  

            if (current_pos[0] + HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))
            
            if (current_pos[0] + HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] + (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] - (MOVE_Y_FOR_FULL_UP + HALF_Y) * numb))


            # rook movement - loop
            if (current_pos[0], current_pos[1] + MOVE_Y_FOR_FULL_UP * numb) in position_list:
                legal_moves.append((current_pos[0], current_pos[1] + MOVE_Y_FOR_FULL_UP * numb))

            if (current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP * numb) in position_list:
                legal_moves.append((current_pos[0], current_pos[1] - MOVE_Y_FOR_FULL_UP * numb))     

            if (current_pos[0] + HALF_X * numb, current_pos[1] + HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] + HALF_Y * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] + HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] + HALF_Y * numb))

            if (current_pos[0] + HALF_X * numb, current_pos[1] - HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] + HALF_X * numb, current_pos[1] - HALF_Y * numb))

            if (current_pos[0] - HALF_X * numb, current_pos[1] - HALF_Y * numb) in position_list:
                legal_moves.append((current_pos[0] - HALF_X * numb, current_pos[1] - HALF_Y * numb))

        return legal_moves

    def stop_collision(self, legal_moves, collides):
        # this stops jumping when moving piece is below the others
        # use bother (x, y) coordinate instead of just y-coord

        for colis in collides:
            if [colis[0] - self.current_pos[0], colis[1] - self.current_pos[1]] in [positive_numbers, negative_numbers]:
                print('yello')
                for moves in legal_moves:
                    if colis[0] < moves[0] and colis[1] > moves[1]:
                        print('yello2')
                        legal_moves.remove(moves)

            
        return legal_moves
                

        
# class Knight(Piece)

class Invis(Piece):
    def __init__(self, color, start_pos, name):
        super().__init__(color, start_pos, name)

    def hide_legal_moves(self, legal):
        None
    def final_draw(self):
        None


# creating pieces 
white_king = King('white', [772, 703], 'king')
white_pawn1 = Pawn('white', [462, 598], 'pawn')
white_pawn2 = Pawn('white', [524, 563], 'pawn')
white_pawn3 = Pawn('white', [586, 528], 'pawn')
white_pawn4 = Pawn('white', [648, 493], 'pawn')
white_pawn5 = Pawn('white', [710, 458], 'pawn')
white_pawn6 = Pawn('white', [772, 493], 'pawn')
white_pawn7 = Pawn('white', [834, 528], 'pawn')
white_pawn8 = Pawn('white', [896, 563], 'pawn')
white_pawn9 = Pawn('white', [958, 598], 'pawn')
white_rook1 = Rook('white', [524, 633],'rook')
white_bishop1 = Bishop('white', [710, 738],'bishop')
white_queen = Queen('white', [648, 703], 'queen')

black_king = King('black', [772, 73],'king')

invisible_piece = Invis('nan', [0, 0], 'nan')

all_pieces = [white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7, white_pawn8, white_king, white_pawn9, white_rook1, white_bishop1, white_queen, black_king]
# Draws the surface object to the screen.
pygame.display.update()

# keep the game looping
running = True
moving = False
 
# Setting what happens when game
# is in running state
while running:
    pygame.display.update()
    for event in pygame.event.get():
        # Close if the user quits the
        # game
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            for piece in all_pieces:
                if piece.coords.collidepoint(event.pos):
                    true_piece = piece
                    moving = True
                    legal = true_piece.check_legal_move(true_piece.current_pos)
                    for pieces in all_pieces:
                        new_legal, collide = true_piece.collide_detect(legal, pieces.current_pos, pieces.color)
                        new_legal_2 = true_piece.stop_collision(new_legal, collide)



                    true_piece.show_legal_moves(new_legal_2)
                    true_piece.final_draw()

            '''
            for piece in pawns:
                # buttons for upgrading (clicking map)
                if piece.qu.collidepoint(event.pos):
                    piece.change_to_queen()
                elif piece.kn.collidepoint(event.pos):
                    piece.change_to_knight()
                elif piece.ro.collidepoint(event.pos):
                    piece.change_to_rook()
                elif piece.bi.collidepoint(event.pos):
                    piece.change_to_bishop()
            '''
    
        elif event.type == MOUSEBUTTONUP:
            if moving == False:
                true_piece = invisible_piece
                new_legal_2 = []
                new_legal = []
                legal = []
            true_piece.hide_legal_moves(new_legal_2)
            true_piece.final_draw()

            for pieces in all_pieces:
                if (true_piece.current_pos[0], true_piece.current_pos[1]) == (pieces.current_pos[0], pieces.current_pos[1]) and true_piece != pieces:
                    all_pieces.remove(pieces)

            for pieces in all_pieces:
                pieces.final_draw()
            moving=False

        elif moving == True:
            for rect in rect_list:
                if (rect.collidepoint(event.pos) and (rect[0], rect[1]) in new_legal_2) or (rect[0], rect[1]) == true_piece.current_pos:
                    true_piece.move(true_piece.current_pos, (rect[0], rect[1]), true_piece.name)
                    true_piece.show_legal_moves(new_legal_2)
                    true_piece.final_draw()
                    moving == False