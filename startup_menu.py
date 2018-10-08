import pygame.font

from alien import Alien


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Menu:

    def __init__(self, ai_settings, screen, play_button, aliens, alien_bullets):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.alien_bullets = alien_bullets

        self.aliens = aliens

        self.button = play_button

        self.menu_color = (190, 190, 190)
        self.text_color = (250, 250, 210)
        self.font = pygame.font.SysFont(None, 48)

        self.title = "Alien Invasion"
        self.score1 = "= 50  pts"
        self.score2 = "= 100 pts"
        self.score3 = "= 200 pts"
        self.score4 = "= ??? pts"

        self.prep_screen()
        self.create_alien()

    def prep_screen(self):
        self.title_image = self.font.render(self.title, True, self.text_color, self.menu_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - 175

        self.score1_image = self.font.render(self.score1, True, self.text_color, self.menu_color)
        self.score1_image_rect = self.score1_image.get_rect()
        self.score1_image_rect.centerx = self.screen_rect.centerx + 50
        self.score1_image_rect.centery = self.screen_rect.centery - 90

        self.score2_image = self.font.render(self.score2, True, self.text_color, self.menu_color)
        self.score2_image_rect = self.score2_image.get_rect()
        self.score2_image_rect.centerx = self.screen_rect.centerx + 50
        self.score2_image_rect.centery = self.screen_rect.centery - 45

        self.score3_image = self.font.render(self.score3, True, self.text_color, self.menu_color)
        self.score3_image_rect = self.score3_image.get_rect()
        self.score3_image_rect.centerx = self.screen_rect.centerx + 50
        self.score3_image_rect.centery = self.screen_rect.centery

        self.score4_image = self.font.render(self.score4, True, self.text_color, self.menu_color)
        self.score4_image_rect = self.score4_image.get_rect()
        self.score4_image_rect.centerx = self.screen_rect.centerx + 50
        self.score4_image_rect.centery = self.screen_rect.centery + 45

    def draw_menu(self):
        self.screen.fill((190, 190, 190))
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.score1_image, self.score1_image_rect)
        self.screen.blit(self.score2_image, self.score2_image_rect)
        self.screen.blit(self.score3_image, self.score3_image_rect)
        self.screen.blit(self.score4_image, self.score4_image_rect)

        self.button.draw_button()
        self.aliens.draw(self.screen)

    def create_alien(self):
        self.ai_settings.alien_index = 8
        alien = Alien(self.ai_settings, self.screen, self.alien_bullets)
        alien.rect.centerx = self.screen_rect.centerx - 50
        alien.rect.centery = self.screen_rect.centery - 100
        self.aliens.add(alien)

        self.ai_settings.alien_index = 4
        alien = Alien(self.ai_settings, self.screen, self.alien_bullets)
        alien.rect.centerx = self.screen_rect.centerx - 50
        alien.rect.centery = self.screen_rect.centery - 50
        self.aliens.add(alien)

        self.ai_settings.alien_index = 0
        alien = Alien(self.ai_settings, self.screen, self.alien_bullets)
        alien.rect.centerx = self.screen_rect.centerx - 50
        alien.rect.centery = self.screen_rect.centery
        self.aliens.add(alien)

        self.ai_settings.alien_index = 12
        alien = Alien(self.ai_settings, self.screen, self.alien_bullets)
        alien.rect.centerx = self.screen_rect.centerx - 50
        alien.rect.centery = self.screen_rect.centery + 50
        self.aliens.add(alien)
