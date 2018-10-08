import pygame.font
from pygame.sprite import Group

from ship import Ship


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Scoreboard:
    def __init__(self, ai_settings, screen, stats, filename, button):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.filename = filename

        self.button = button

        self.scores = []

        self.text_color = (250, 250, 210)
        self.font = pygame.font.SysFont(None, 48)

        self.get_scores()

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "High score: {:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        current_level = self.stats.level
        current_level_str = "Level: {:,}".format(current_level)
        self.level_image = self.font.render(current_level_str, True, self.text_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def get_scores(self):
        with open(self.filename, 'r+') as f:
            self.rows = f.readlines()
        self.fill()
        self.stats.high_score = int(self.scores[0])

    def fill(self):
        for nrow in range(len(self.rows)):
            temp_score = self.rows[nrow]
            self.scores.append(temp_score)

    def prep_list(self):
        self.title_image = self.font.render("Alien Invasion High Scores", True, self.text_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - 175

        self.one_image = self.font.render("1. {:s}".format(self.scores[0]), True, self.text_color)
        self.one_image_rect = self.one_image.get_rect()
        self.one_image_rect.centerx = self.screen_rect.centerx
        self.one_image_rect.centery = self.screen_rect.centery - 125

        self.two_image = self.font.render("2. {:s}".format(self.scores[1]), True, self.text_color)
        self.two_image_rect = self.two_image.get_rect()
        self.two_image_rect.centerx = self.screen_rect.centerx
        self.two_image_rect.centery = self.screen_rect.centery - 75

        self.three_image = self.font.render("3. {:s}".format(self.scores[2]), True, self.text_color)
        self.three_image_rect = self.three_image.get_rect()
        self.three_image_rect.centerx = self.screen_rect.centerx
        self.three_image_rect.centery = self.screen_rect.centery - 25

        self.four_image = self.font.render("4. {:s}".format(self.scores[3]), True, self.text_color)
        self.four_image_rect = self.four_image.get_rect()
        self.four_image_rect.centerx = self.screen_rect.centerx
        self.four_image_rect.centery = self.screen_rect.centery + 25

        self.five_image = self.font.render("5. {:s}".format(self.scores[4]), True, self.text_color)
        self.five_image_rect = self.five_image.get_rect()
        self.five_image_rect.centerx = self.screen_rect.centerx
        self.five_image_rect.centery = self.screen_rect.centery + 75

        self.button.draw_button()

    def display_list(self):
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.one_image, self.one_image_rect)
        self.screen.blit(self.two_image, self.two_image_rect)
        self.screen.blit(self.three_image, self.three_image_rect)
        self.screen.blit(self.four_image, self.four_image_rect)
        self.screen.blit(self.five_image, self.five_image_rect)

    def check_leaderboard(self):
        for gstats in range(5):
            if self.stats.score > int(self.scores[gstats]):
                self.scores[gstats] = str(self.stats.score)
