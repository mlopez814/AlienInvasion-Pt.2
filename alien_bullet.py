import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):

    def __init__(self, ai_settings, screen, alien_rect):
        super(AlienBullet, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.alien_rect = alien_rect

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.y = float(self.alien_rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
