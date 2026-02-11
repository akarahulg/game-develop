#!/usr/bin/env python3
import pygame
from settings import *
from game import Game
from bird import Bird
from pipe import Pipe

class FlappyBird:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((GAME_WIDTH , GAME_HEIGHT))
        pygame.display.set_caption('FlappyBird')

        self.clock = pygame.time.Clock()
        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, TICK)

        self.running = True
        self.game = Game()
        self.start = False

        self.start_image = pygame.image.load('assets/sprites/message.png').convert_alpha()
        self.start_image = pygame.transform.scale(
                                    self.start_image,
                                    (self.start_image.get_width() * 1.5,
                                    self.start_image.get_height() * 1.5)
                                    )
        self.start_rect = self.start_image.get_rect(
                                center=(GAME_WIDTH // 2, GAME_HEIGHT // 2)
                                  )


        self.bkg = pygame.image.load('assets/sprites/background-day.png').convert_alpha()
        self.bkg = pygame.transform.scale(self.bkg, (GAME_WIDTH, GAME_HEIGHT))
        self.bkg_rect = self.bkg.get_rect(topleft=[0,0])

    def start_screen(self):
        self.display_surface.blit(self.bkg, self.bkg_rect)
        self.display_surface.blit(self.start_image, self.start_rect)
        

    def run(self):
        while self.running:
            if not self.start:
                self.start_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.start = True
            else:
                self.game.run()
                for event in pygame.event.get():
                    self.game.handle_events(event)
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.game.bird.flap()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    flappybird = FlappyBird()
    flappybird.run()



