import pygame
from sudoku_generator import generate_sudoku, SudokuGenerator
from cell import Cell

class Board():
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.rows = 9
        self.cols = 9
        self.ROWS = 9
        self.COLS = 9
        
        # Generate the sudoku puzzle and solution
        # We need to generate the solution first, then remove cells to get the puzzle
        generator = SudokuGenerator(9, difficulty)
        generator.fill_values()
        self.solution = [row[:] for row in generator.get_board()]  # Store solution before removing cells
        generator.remove_cells()
        self.board = [row[:] for row in generator.get_board()]  # Puzzle with removed cells
        
        # Create a copy for the original board state (with removed cells)
        self.original_board = [row[:] for row in self.board]  # Deep copy
        
        # Model represents current state
        self.model = [row[:] for row in self.board]  # Deep copy
        
        # Create Cell objects
        self.cells = []
        cell_size = min(width // 9, height // 9)
        for row in range(9):
            cell_row = []
            for col in range(9):
                cell = Cell(self.board[row][col], row, col, screen)
                cell.size = cell_size
                cell_row.append(cell)
            self.cells.append(cell_row)
        
        # Track selected cell
        self.selected = None
        
        # Track which cells are editable (not pre-filled)
        self.editable = [[self.board[row][col] == 0 for col in range(9)] for row in range(9)]
    
    def draw(self):
        # Draw background
        cell_size = min(self.width // 9, self.height // 9)
        
        # Update cell sizes to match
        for row in range(9):
            for col in range(9):
                self.cells[row][col].size = cell_size
                self.cells[row][col].draw()
        
        # Draw grid lines
        BLACK = (0, 0, 0)
        LIGHT_GRAY = (200, 200, 200)  # Lighter color for intermediate lines
        board_size = 9 * cell_size
        for i in range(10):
            # Vertical lines - thicker and black for 3x3 box boundaries, thin and gray for intermediate
            x = i * cell_size
            if i % 3 == 0:
                line_width = 5
                line_color = BLACK
            else:
                line_width = 1
                line_color = LIGHT_GRAY
            pygame.draw.line(self.screen, line_color, (x, 0), (x, board_size), line_width)
            
            # Horizontal lines - thicker and black for 3x3 box boundaries, thin and gray for intermediate
            y = i * cell_size
            pygame.draw.line(self.screen, line_color, (0, y), (board_size, y), line_width)

    def select(self, row, col):
        # Deselect previous cell
        if self.selected:
            prev_row, prev_col = self.selected
            self.cells[prev_row][prev_col].selected = False
        
        # Select new cell
        self.selected = (row, col)
        self.cells[row][col].selected = True

    def click(self, x, y):
        cell_size = min(self.width // 9, self.height // 9)
        board_size = 9 * cell_size
        
        # Check if click is within board bounds
        if x < 0 or x > board_size or y < 0 or y > board_size:
            return None
        
        # Calculate which cell was clicked
        col = int(x // cell_size)
        row = int(y // cell_size)
        
        # Ensure valid indices
        if 0 <= row < 9 and 0 <= col < 9:
            return (row, col)
        return None

    def clear(self):
        if self.selected:
            row, col = self.selected
            # Only clear if cell is editable
            if self.editable[row][col]:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(0)
                self.update_board()
 
    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            # Only sketch if cell is editable
            if self.editable[row][col]:
                self.cells[row][col].set_sketched_value(value)
    
    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            # Only place if cell is editable
            if self.editable[row][col]:
                self.cells[row][col].set_cell_value(value)
                self.cells[row][col].set_sketched_value(0)  # Clear sketch when placing
                self.update_board()

    def reset_to_original(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.model[r][c] = self.original_board[r][c]
                self.cells[r][c].set_cell_value(self.original_board[r][c])
                self.cells[r][c].set_sketched_value(0)
   
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
        # Check rows
        for row in self.model:
            if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
        
        # Check columns
        for c in range(self.COLS):
            col = [self.model[r][c] for r in range(self.ROWS)]
            if sorted(col) != list(range(1, 10)):
                return False
        
        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                nums = []
                for r in range(3):
                    for c in range(3):
                        nums.append(self.model[box_row + r][box_col + c])
                if sorted(nums) != list(range(1, 10)):
                    return False
        
        return True
    
    def move_selection(self, direction):
        if not self.selected:
            # If nothing selected, select top-left
            self.select(0, 0)
            return
        
        row, col = self.selected
        
        if direction == "up":
            row = max(0, row - 1)
        elif direction == "down":
            row = min(8, row + 1)
        elif direction == "left":
            col = max(0, col - 1)
        elif direction == "right":
            col = min(8, col + 1)
        
        self.select(row, col)
