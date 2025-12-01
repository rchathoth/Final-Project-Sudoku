import pygame
from sudoku_generator import generate_sudoku
from board import Board
from cell import Cell

# CONSTANTS
WIDTH, HEIGHT = 600, 700  
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
        pygame.draw.rect(win, BLACK, self.rect, 2)  
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

