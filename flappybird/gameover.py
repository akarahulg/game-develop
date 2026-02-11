import pygame
from settings import *

class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
        self.rect = self.image.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2))