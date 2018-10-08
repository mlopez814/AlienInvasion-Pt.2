import pygame
from pygame.sprite import Sprite


def load_image(self):
    image = pygame.image.load(self)
    return image


class UFO(Sprite):

    def __init__(self, ai_settings, screen):
        super(UFO, self).__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        self.images = []
        self.images.append(load_image('images/Aliens/ufo1.png'))
        self.images.append(load_image('images/Aliens/ufo1.png'))
        self.images.append(load_image('images/Aliens/ufo2.png'))
        self.images.append(load_image('images/Aliens/ufo2.png'))

        self.index = ai_settings.UFO_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = -20
        self.rect.y = 10

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True

    def update(self):
        self.x += self.ai_setting.ufo_speed_factor
        self.rect.x = self.x

        self.index += 1
        if self.index >= 4:
            self.index = 0
        self.image = self.images[self.index]
