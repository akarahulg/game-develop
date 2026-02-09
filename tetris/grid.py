import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_block_colors()
        self.complete_rows = []

    def is_empty(self, row, col):
        if self.grid[row][col] != 0:
            return False
        return True
    
    def is_row_full(self, row):
        for col in range(self.num_cols):
            if all(x != 0 for x in self.grid[row]):
                self.complete_rows.append(row)
                return True
        return False
    
    def clear_rows(self):
        for row in self.complete_rows:
            del self.grid[row]
            self.grid.insert(0, [0 for i in range(self.num_cols)])
        self.complete_rows = []

    def reset(self):
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.complete_rows = []
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cellValue =  self.grid[row][col]
                cellBlock = pygame.Rect(self.cell_size*col+1, self.cell_size*row+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cellValue], cellBlock)
                
    
    

