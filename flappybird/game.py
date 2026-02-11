import pygame
from settings import *
from pipe import Pipe
from random import randint
from bird import Bird
from score import Score
from gameover import Gameover

class Game():
    def __init__(self): 

        self.display_surface = pygame.display.get_surface()

        self.bkg = pygame.image.load('assets/sprites/background-day.png').convert_alpha()
        self.bkg = pygame.transform.scale(self.bkg, (GAME_WIDTH, GAME_HEIGHT))

        self.base = pygame.image.load('assets/sprites/base.png').convert_alpha()
        _ , self.base_height =  self.base.get_size()
        self.base = pygame.transform.scale(self.base, (GAME_WIDTH + 32, self.base_height))

        self.bkg_rect = self.bkg.get_rect()
        self.bkg_rect.topleft = [0,0]

        self.base_rect = self.base.get_rect()
        self.base_rect.bottomright = [GAME_WIDTH + 32, GAME_HEIGHT]

        self.bird = Bird((99, GAME_HEIGHT //2))
        self.bird_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.bird_group.add(self.bird)

        self.fly = True
        
        self.score = 0
        self.score_sprite = Score()
 
        self.now = pygame.time.get_ticks()
        
    def run(self):

        if self.fly:
            self.base_rect.x -= SCROLL_SPEED

        if self.base_rect.x <= -30:
            self.base_rect.bottomright = [GAME_WIDTH + 32, GAME_HEIGHT]

        self.display_surface.blit(self.bkg, self.bkg_rect)
        
        self.pipe_group.update(self.fly)
        self.pipe_group.draw(self.display_surface)
        self.display_surface.blit(self.base, self.base_rect)

        self.bird_group.update(self.fly)
        self.update()
        self.bird_group.draw(self.display_surface)
        self.check_crash()
        self.increase_score()
        self.collide_check()
        self.gameover()

    def update(self):

        if self.fly:
            if abs(self.now - pygame.time.get_ticks()) > PIPE_FREQUENCY:
                self.add_pipe()
                self.now = pygame.time.get_ticks()

    def add_pipe(self):
        offset = randint(-1*OFFSET, OFFSET)
        self.pipe_group.add(Pipe(GAME_WIDTH, GAME_HEIGHT //2 - 50, flipped=True, center=offset))
        self.pipe_group.add(Pipe(GAME_WIDTH, GAME_HEIGHT //2 - 50, flipped=False, center=offset))

    def collide_check(self):
        collision = pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False)
        if collision:
            self.fly = False

    def check_crash(self):
        if self.bird.rect.bottom >= self.base_rect.top:
            self.fly = False   
    
    def increase_score(self):
        for pipe in self.pipe_group:
            if pipe.passed is False and pipe.rect.right < self.bird.rect.left:
                pipe.passed = True
                self.score += 0.5 
                
        self.score_sprite.draw_score(int(self.score))
    
    def gameover(self):
        if not self.fly:
            self.gameover_sprite = Gameover()
            self.display_surface.blit(self.gameover_sprite.image, self.gameover_sprite.rect)



















