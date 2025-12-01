import pygame

class Board():
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    
    def draw(self):
        hi = self.height / 9
        wi = self.width / 9
        for i in range(9):
            pygame.draw.line(self.screen, "black", (i*wi, 0), (i*wi, self.height) )
        
        

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass
 
    def sketch(self, value):
        pass
     
    def place_number(self, value):
        pass
    
    def reset_to_original(self):
        pass
   
    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

