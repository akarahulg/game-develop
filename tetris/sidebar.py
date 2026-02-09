import pygame
from colors import Colors

class Sidebar:
    def __init__(self, next_block):
        self.width = 200
        self.height = 600
        self.next_block = next_block
        self.colors = Colors.get_block_colors()
        self.next_block_surface = pygame.Surface((self.width, self.height))
        self.main_surface = pygame.display.get_surface()
        self.next_block_surface.fill(self.colors[0])

    def run(self):
        self.main_surface.blit(self.next_block_surface, (350, 10))
        self.next_block.draw(self.next_block_surface)



    
