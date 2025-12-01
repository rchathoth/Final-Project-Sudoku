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
        if self.selected:
            row, col = self.selected
            cell = self.cells[row][col]
            if cell.value == 0:
                cell.set_value(value)
                self.update_board()

    def reset_to_original(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.model[r][c] = self.original_board[r][c]
   
    def is_full(self):
        for row in self.model:
            for val in row:
                if val == 0:
                    return False
        return True

    def update_board(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.model[r][c] = self.cells[r][c].value

    def find_empty(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.model[r][c] == 0:
                    return (r, c)
        return None

    def check_board(self):
        # checks rows
        for row in self.model:
             if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                 return False
        
        # checks columns
        for c in range(self.COLS):
            col = [self.model[r][c] for r in range(self.ROWS)]
            if sorted(col) != list(range(1, 10)):
                return False
            for box_row in range(0, 9, 3):
        
        # checks 3x3 boxes
        for box_col in range(0, 9, 3):
            nums = []
            for r in range(3):
                for c in range(3):
                    nums.append(self.model[box_row + r][box_col + c])
            if sorted(nums) != list(range(1, 10)):
                return False
        
        return True
