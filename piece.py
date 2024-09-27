import pygame

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