class Board():
    def __init__(self, width, height, screen, difficulty):
        pass
    
    def draw(self):
        pass

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
        print("hello world")    
