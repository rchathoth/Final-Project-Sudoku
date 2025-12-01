import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0          
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.size = 60  # Default, will be updated by Board

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * self.size
        y = self.row * self.size


        border_color = (255, 0, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(self.screen, border_color, (x, y, self.size, self.size), 2)

        big_font = pygame.font.SysFont("arial", 40)
        small_font = pygame.font.SysFont("arial", 20)


        if self.value != 0:
            text = big_font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + 30, y + 30))
            self.screen.blit(text, text_rect)


        elif self.sketched_value != 0:
            text = small_font.render(str(self.sketched_value), True, (150, 150, 150))
            self.screen.blit(text, (x + 5, y + 5))
