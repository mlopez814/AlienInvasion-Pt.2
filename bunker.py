import pygame
from pygame.sprite import Sprite


def load_image(self):
    image = pygame.image.load(self)
    return image


class Bunker(Sprite):

    def __init__(self, ai_settings, screen, alien_bullets):
        super(Bunker, self).__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        self.alien_bullets = alien_bullets

        self.images = []
        self.images.append(load_image('images/bunker/bunker0.png'))
        self.images.append(load_image('images/bunker/bunker1.png'))
        self.images.append(load_image('images/bunker/bunker2.png'))
        self.images.append(load_image('images/bunker/bunker3/flashing_red0.png'))
        self.images.append(load_image('images/bunker/bunker3/flashing_red1.png'))
        self.images.append(load_image('images/bunker/bunker3/flashing_red2.png'))
        self.images.append(load_image('images/bunker/bunker3/flashing_red3.png'))
        self.images.append(load_image('images/bunker/bunker3/flashing_red4.png'))

        self.index = ai_settings.bunker_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.animate()

    def animate(self):
        self.index += 1
        if self.index == 1:
            self.index = 0
        if self.index > 1 and self.index == 2:
            self.index = 1
        if self.index > 2 and self.index == 3:
            self.index = 2
        if self.index > 3 and self.index >= 7:
            self.index = 3
        self.image = self.images[self.index]
