import pygame
from sudoku_generator import generate_sudoku
from board import Board
from cell import Cell

# CONSTANTS
WIDTH, HEIGHT = 600, 700  # Increased height for buttons
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# BUTTON CLASS
class Button:
    def __init__(self, text, x, y, width, height, font_size=30):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.font = pygame.font.SysFont("comicsans", font_size)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, BLACK, self.rect, 2)  # Border
        txt = self.font.render(self.text, True, BLACK)
        win.blit(txt, (self.rect.x + self.rect.width/2 - txt.get_width()/2,
                    self.rect.y + self.rect.height/2 - txt.get_height()/2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# START SCREEN
def start_screen(screen):
    font = pygame.font.SysFont("comicsans", 60)
    title = font.render("Welcome to Sudoku", True, BLACK)
    
    easy_btn = Button("Easy", 200, 250, 200, 60)
    medium_btn = Button("Medium", 200, 350, 200, 60)
    hard_btn = Button("Hard", 200, 450, 200, 60)
    buttons = [easy_btn, medium_btn, hard_btn]

    selecting = True
    difficulty = 0
    while selecting:
        screen.fill(WHITE)
        screen.blit(title, (WIDTH/2 - title.get_width()/2, 100))
        
        for btn in buttons:
            btn.draw(screen)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if easy_btn.is_clicked(pos):
                    difficulty = 30
                    selecting = False
                elif medium_btn.is_clicked(pos):
                    difficulty = 40
                    selecting = False
                elif hard_btn.is_clicked(pos):
                    difficulty = 50
                    selecting = False

    return difficulty

# WIN SCREEN
def win_screen(screen):
    font_large = pygame.font.SysFont("comicsans", 60)
    font_small = pygame.font.SysFont("comicsans", 40)
    title = font_large.render("Game Won!", True, GREEN)
    subtitle = font_small.render("Press any key to exit", True, BLACK)
    
    waiting = True
    while waiting:
        screen.fill(WHITE)
        screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - 50))
        screen.blit(subtitle, (WIDTH/2 - subtitle.get_width()/2, HEIGHT/2 + 50))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return False
    
    return False

# LOSE SCREEN
def lose_screen(screen):
    font_large = pygame.font.SysFont("comicsans", 60)
    font_small = pygame.font.SysFont("comicsans", 40)
    title = font_large.render("Game Over :(", True, RED)
    subtitle = font_small.render("Press any key to exit", True, BLACK)
    
    waiting = True
    while waiting:
        screen.fill(WHITE)
        screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - 50))
        screen.blit(subtitle, (WIDTH/2 - subtitle.get_width()/2, HEIGHT/2 + 50))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return False
    
    return False

# MAIN FUNCTION
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    
    # Game state: 'start', 'playing', 'won', 'lost'
    game_state = 'start'
    board = None
    
    running = True
    while running:
        if game_state == 'start':
            # Show start screen and get difficulty
            removed_cells = start_screen(screen)
            if removed_cells is None:  # User closed window
                running = False
                break
            
            # Initialize board
            board = Board(WIDTH, HEIGHT - 100, screen, removed_cells)  # Reserve space for buttons
            game_state = 'playing'
        
        elif game_state == 'playing':
            screen.fill(WHITE)
            
            # Draw board
            board.draw()
            
            # Create buttons below the board
            button_y = HEIGHT - 80
            reset_btn = Button("Reset", 50, button_y, 120, 50)
            restart_btn = Button("Restart", 240, button_y, 120, 50)
            exit_btn = Button("Exit", 430, button_y, 120, 50)
            
            reset_btn.draw(screen)
            restart_btn.draw(screen)
            exit_btn.draw(screen)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Mouse click to select a cell or click buttons
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    
                    # Check button clicks
                    if reset_btn.is_clicked(pos):
                        board.reset_to_original()
                    elif restart_btn.is_clicked(pos):
                        game_state = 'start'
                    elif exit_btn.is_clicked(pos):
                        running = False
                    else:
                        # Check cell clicks
                        clicked = board.click(*pos)
                        if clicked:
                            row, col = clicked
                            board.select(row, col)
                
                # Keyboard input
                if event.type == pygame.KEYDOWN:
                    # Numbers 1-9: sketch the value
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        num = event.key - pygame.K_0
                        board.sketch(num)
                    
                    # Enter/Return: submit sketched value
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if board.selected:
                            row, col = board.selected
                            cell = board.cells[row][col]
                            if cell.sketched_value != 0:
                                board.place_number(cell.sketched_value)
                    
                    # Delete/Backspace: clear cell
                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        board.clear()
                    
                    # Arrow key navigation
                    elif event.key == pygame.K_UP:
                        board.move_selection("up")
                    elif event.key == pygame.K_DOWN:
                        board.move_selection("down")
                    elif event.key == pygame.K_LEFT:
                        board.move_selection("left")
                    elif event.key == pygame.K_RIGHT:
                        board.move_selection("right")
            
            # Check for win/lose conditions
            if board.is_full():
                if board.check_board():
                    game_state = 'won'
                else:
                    game_state = 'lost'
        
        elif game_state == 'won':
            if not win_screen(screen):
                running = False
        
        elif game_state == 'lost':
            if not lose_screen(screen):
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
