import pygame 
from colors import Colors
from position import Position


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.row_offset = 0
        self.col_offset = 0
        self.colors = Colors.get_block_colors()

    def draw(self, screen ,offx, offy):
        tiles = self.updated_tile_positions()
        for tile in tiles:
            cellBlock = pygame.Rect(offx + tile.col*self.cell_size + 1, offy + tile.row*self.cell_size + 1 , self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], cellBlock)
            
    
    def rotate(self):
        self.rotation_state = (self.rotation_state + 1) % len(self.cells)
    
    def rotate_back(self):
        self.rotation_state = (self.rotation_state - 1) % len(self.cells)
    
    def move(self, row, col):
        self.row_offset += row
        self.col_offset += col

    def updated_tile_positions(self):
        tiles = self.cells[self.rotation_state]
        updated_tiles = []
        for tile in tiles:
            updated_tile = Position(tile.row + self.row_offset, tile.col + self.col_offset)
            updated_tiles.append(updated_tile)
        return updated_tiles    


    
