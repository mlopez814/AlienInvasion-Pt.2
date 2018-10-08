# noinspection PyAttributeOutsideInit
class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 200, 200)
        self.bullets_allowed = 3

        self.ship_limit = 3

        self.fire_last = 0
        self.ufo_last = 0

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1

        self.alien_index = 0
        self.UFO_index = 0
        self.bunker_index = 0
        self.ship_index = 0

        self.initialize_dynamic_settings()

    # noinspection PyAttributeOutsideInit
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 5
        self.ufo_speed_factor = 7
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 3
        self.fleet_direction = 1

        self.alien_points = 50
        self.ufo_points = 500

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
