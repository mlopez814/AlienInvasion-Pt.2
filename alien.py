from random import randint

import pygame
from pygame.sprite import Sprite

from alien_bullet import AlienBullet


def load_image(self):
    image = pygame.image.load(self)
    return image


class Alien(Sprite):

    def __init__(self, ai_settings, screen, alien_bullets):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        self.alien_bullets = alien_bullets

        self.images = []
        self.images.append(load_image('images/Aliens/sprite_0.png'))
        self.images.append(load_image('images/Aliens/sprite_0.png'))
        self.images.append(load_image('images/Aliens/sprite_1.png'))
        self.images.append(load_image('images/Aliens/sprite_1.png'))
        self.images.append(load_image('images/Aliens/sprite_4.png'))
        self.images.append(load_image('images/Aliens/sprite_4.png'))
        self.images.append(load_image('images/Aliens/sprite_5.png'))
        self.images.append(load_image('images/Aliens/sprite_5.png'))
        self.images.append(load_image('images/Aliens/sprite_6.png'))
        self.images.append(load_image('images/Aliens/sprite_6.png'))
        self.images.append(load_image('images/Aliens/sprite_7.png'))
        self.images.append(load_image('images/Aliens/sprite_7.png'))

        self.images.append(load_image('images/Aliens/ufo1.png'))

        self.images.append(load_image('images/Aliens/explosion/explosion0.png'))
        self.images.append(load_image('images/Aliens/explosion/explosion1.png'))
        self.images.append(load_image('images/Aliens/explosion/explosion2.png'))
        self.images.append(load_image('images/Aliens/explosion/explosion3.png'))
        self.images.append(load_image('images/Aliens/explosion/explosion4.png'))

        self.index = ai_settings.alien_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_setting.alien_speed_factor *
                   self.ai_setting.fleet_direction)
        self.rect.x = self.x

        random_number = randint(2000, 3000)
        now = pygame.time.get_ticks()

        if now - self.ai_setting.fire_last > random_number:
                now = pygame.time.get_ticks()
                self.fire_bullet()
                self.ai_setting.fire_last = now

        self.animate()

    def fire_bullet(self):
        new_bullet = AlienBullet(self.ai_setting, self.screen, self.rect)
        new_bullet.rect.centerx = self.rect.centerx
        new_bullet.rect.top = self.rect.bottom
        new_bullet.rect.y = self.rect.y
        self.alien_bullets.add(new_bullet)

    def animate(self):
        self.index += 1
        if self.index == 4:
            self.index = 0
        if self.index > 4 and self.index == 8:
            self.index = 4
        if self.index > 8 and self.index == 12:
            self.index = 8
        if self.index > 12 and self.index >= 16:
            self.index = 12
        self.image = self.images[self.index]
