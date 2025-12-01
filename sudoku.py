import pygame as game
from sudoku_generator import SudokuGenerator

def main():

    game.init()
    screen = game.display.set_mode((600, 600))
    game.display.set_caption("Sudoku")
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
    game.quit()



if __name__ == "__main__":
    main()