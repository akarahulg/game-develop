from blocks import *
import pygame
import random
from colors import Colors
from grid import Grid
from sys import exit
from settings import *

class Game:
    def __init__(self):
        self.grid = Grid()
        self.colors = Colors.get_block_colors()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # self.blocks = [OBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))        
        self.main_surface = pygame.display.get_surface()
        self.score = 0
        self.gameover = False

    def update_score(self):
        if len(self.grid.complete_rows) == 1:
            self.score += 100
        elif len(self.grid.complete_rows) == 2:
            self.score += 300
        elif len(self.grid.complete_rows) == 3:
            self.score += 500
        elif len(self.grid.complete_rows) >= 4:
            self.score += 800

    def move_left(self):
        self.current_block.move(0, -1)
        if self.inside_grid() == False or self.is_block_fit() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.inside_grid() == False or self.is_block_fit() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.inside_grid() == False or self.is_block_fit() == False:
            self.current_block.move(-1,0)
            self.lock_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
            # self.blocks = [OBlock()]
        selected = random.choice(self.blocks)
        self.blocks.remove(selected)
        return selected

    def rotate(self):
        self.current_block.rotate()
        if self.inside_grid() == False or self.is_block_fit() == False:
            self.current_block.rotate_back()
    
    def inside_grid(self):
        tiles = self.current_block.updated_tile_positions()
        for tile in tiles:
            if tile.row < 0 or tile.row >= self.grid.num_rows or tile.col < 0 or tile.col >= self.grid.num_cols:
                return False
        return True
    
    def lock_block(self):
        tiles = self.current_block.updated_tile_positions()
        for tile in tiles:
            self.grid.grid[tile.row][tile.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        for row in range(self.grid.num_rows):
            self.grid.is_row_full(row)
        if len(self.grid.complete_rows) > 0:
            self.update_score()
            self.grid.clear_rows()
        if self.is_block_fit() == False:
            self.gameover = True

    def is_block_fit(self):
        tiles = self.current_block.updated_tile_positions() 
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.col) is False:
                return False
        return True       

    def restart(self):
        self.grid.reset()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.gameover = False

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 0, 0)
