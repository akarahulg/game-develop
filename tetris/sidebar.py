import pygame
from colors import Colors
from settings import *

class Sidebar:
    def __init__(self, next_block):
        self.next_block = next_block
        self.cell_size = 30  # Adjust this to match your block's cell size
        self.next_block_surface = pygame.Surface((SIDE_WIDTH, (SIDE_BAR_FRACTION) * GAME_HEIGHT))
        self.main_surface = pygame.display.get_surface()

    def run(self):
        self.next_block_surface.fill(Colors.TETRIS_COLORS["-"])
        self.next_block.draw(self.next_block_surface, -40, 60)
        self.main_surface.blit(self.next_block_surface, (GAME_WIDTH + PADDING*2, PADDING))





    
