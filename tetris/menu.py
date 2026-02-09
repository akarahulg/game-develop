from settings import *
import pygame
from button import Button
from colors import Colors

class Menu:
    def __init__(self, game):
        self.game = game
        self.main_surface = pygame.display.get_surface()
        self.menu_surface = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
        self.start_button = Button(0, 0, 150, 40, "RESTART", Colors.TETRIS_COLORS['-'], self.game.restart)
        self.quit_button = Button(0, 20 , 150, 40, "QUIT", Colors.TETRIS_COLORS['-'], pygame.quit)
    
    def run(self):
        self.menu_surface.fill(Colors.TETRIS_COLORS["-"])
        self.start_button.draw(self.menu_surface)
        self.quit_button.draw(self.menu_surface)
        self.main_surface.blit(self.menu_surface, (self.main_surface.get_width() // 2 - MENU_WIDTH // 2, self.main_surface.get_height() // 2 - MENU_HEIGHT // 2))
        self.start_button.perform_left_click_action()
        self.quit_button.perform_left_click_action()
