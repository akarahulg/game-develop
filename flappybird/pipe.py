import pygame
from settings import *

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y , flipped=False, center=0):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height + 200))
        self.rect = self.image.get_rect()

        if flipped:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y - center - PIPE_GAP // 2]
        else:
            self.rect.topleft = [x,y - center + PIPE_GAP // 2]
        
        self.passed = False
            

    def update(self, fly):
        if fly:
            self.rect.x -= SCROLL_SPEED
        if self.rect.x <= -50:
            self.kill()


