import pygame
from settings import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.frames = [
            pygame.image.load(f'assets/sprites/{f}.png').convert_alpha() for f in range(10)
        ]
        
    def draw_score(self, score):
        score_str = str(score)
        for i, digit in enumerate(score_str):
            digit_image = self.frames[int(digit)]
            digit_rect = digit_image.get_rect()
            digit_rect.center = (GAME_WIDTH // 2 - 20 + i * digit_image.get_width(), 50)
            self.display_surface.blit(digit_image, digit_rect)
    