#!/usr/bin/env python3

"""
Learn pygame
"""

import sys
import pygame
from game import Game

pygame.init()

GRAY = (22, 22, 22)
size = width, height = 300, 600  
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TETRIS')

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200) 

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                game.rotate()
            if event.key == pygame.K_h:
                game.move_left()
            if event.key == pygame.K_l:
                game.move_right()
            if event.key == pygame.K_j:
                game.move_down()
        if event.type == GAME_UPDATE:
            game.move_down()
            
    screen.fill(GRAY)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
