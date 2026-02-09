import pygame
from settings import *


class Gameover:
    def __init__(self, game):
        self.game = game
        self.gameover_surface = pygame.Surface((GAME_OVER_WIDTH, GAME_OVER_HEIGHT))
        self.main_surface = pygame.display.get_surface()

    def run(self):
        if self.game.gameover:      
            self.gameover_surface.fill((0, 0, 0))
            font = pygame.font.SysFont('Arial', 30)
            gameover_text = font.render("Game Over", True, (255, 255, 255))
            self.gameover_surface.blit(gameover_text, (self.gameover_surface.get_width() // 2 - gameover_text.get_width() // 2,
                                                   self.gameover_surface.get_height() // 2 - gameover_text.get_height() // 2))
            self.main_surface.blit(self.gameover_surface, (GAME_WIDTH // 2 - GAME_OVER_WIDTH // 2,
                                                       GAME_HEIGHT // 2 - GAME_OVER_HEIGHT // 2))