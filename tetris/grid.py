import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_block_colors()

    def is_empty(self, row, col):
        if self.grid[row][col] != 0:
            return False
        return True
    
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cellValue =  self.grid[row][col]
                cellBlock = pygame.Rect(self.cell_size*col+1, self.cell_size*row+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cellValue], cellBlock)
                
    
    

