import pygame
from pygame.sprite import Sprite


def load_image(self):
    image = pygame.image.load(self)
    return image


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(load_image('images/myShip/ship00.png'))
        self.images.append(load_image('images/myShip/ship01.png'))
        self.images.append(load_image('images/myShip/ship02.png'))
        self.images.append(load_image('images/myShip/ship03.png'))
        self.images.append(load_image('images/myShip/ship04.png'))
        self.images.append(load_image('images/myShip/ship05.png'))
        self.images.append(load_image('images/myShip/ship06.png'))
        self.images.append(load_image('images/myShip/ship07.png'))
        self.images.append(load_image('images/myShip/ship08.png'))
        self.images.append(load_image('images/myShip/ship09.png'))
        self.images.append(load_image('images/myShip/ship10.png'))

        self.index = ai_settings.ship_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

        self.animate()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def animate(self):
        self.index += 1
        if self.index == 1:
            self.index = 0
        if self.index > 1 and self.index >= 11:
            self.index = 1
        self.image = self.images[self.index]
