#!/usr/bin/env python3

"""
Learn pygame
"""

import sys
import pygame
from game import Game
from sidebar import Sidebar
from settings import *
from scoreboard import Score
from gameover import Gameover
from menu import Menu


class Tetris:
    def __init__(self):
        pygame.init()
        self.GRAY = (22, 22, 22)
        self.size = self.width, self.height = GAME_WIDTH + SIDE_WIDTH + PADDING * 3, GAME_HEIGHT + PADDING * 2
        self.main_screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('TETRIS')

        self.clock = pygame.time.Clock()
        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, 200)

        # Components
        self.game = Game()
        self.scoreboard = Score(self.game)
        self.gameover = Gameover(self.game) 
        self.Menu = Menu(self.game) 

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.game.gameover is False:
                        self.game.rotate()
                    if event.key == pygame.K_LEFT and self.game.gameover is False:
                        self.game.move_left()
                    if event.key == pygame.K_RIGHT and self.game.gameover is False:
                        self.game.move_right()
                    if event.key == pygame.K_DOWN and self.game.gameover is False:
                        self.game.move_down()
                if event.type == self.GAME_UPDATE and self.game.gameover is False:
                    self.game.move_down()
                    
            self.main_screen.fill(self.GRAY)
            self.game.draw(self.game.game_surface)
            self.main_screen.blit(self.game.game_surface, (PADDING, PADDING))
            self.next_block = self.game.next_block
            self.sidebar = Sidebar(self.next_block)
            self.sidebar.run()
            self.scoreboard.run()
            self.gameover.run()
            self.Menu.run()


            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    tetris = Tetris()
    tetris.run()