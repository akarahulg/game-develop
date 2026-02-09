import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, action, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont('Arial', self.font_size)
        self.color = color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)  # Button color
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_left_clicked(self, pos, mouse_button):
        if self.rect.collidepoint(pos) and mouse_button == 1:
            return True
        return False
    
    def perform_left_click_action(self):
        if self.is_left_clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0]):
            self.action()


    
