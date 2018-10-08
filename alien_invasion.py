import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from startup_menu import Menu
from ufo import UFO
import game_functions as gf


# noinspection SpellCheckingInspection
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(screen, "Play", "Highscores")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats, 'images/highscores.txt', play_button)

    ship = Ship(ai_settings, screen)
    ufo = Group()
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    bunkers = Group()

    pygame.mixer.music.load('sounds/winter.wav')
    pygame.mixer.music.play(-1)

    menu = Menu(ai_settings, screen, play_button, aliens, alien_bullets)

    gf.create_ufo(ai_settings, screen, aliens, alien_bullets)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, alien_bullets, bunkers)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo, bunkers)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo)
            gf.update_ufo(ai_settings, screen, ufo)
            gf.update_bunker(bunkers)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo, bunkers)


run_game()
