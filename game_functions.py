import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien
from ufo import UFO
from random import randint
from bunker import Bunker


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, alien_bullets, bunkers):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                              bullets, mouse_x, mouse_y, alien_bullets, bunkers)


# noinspection PyPep8Naming
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y, alien_bullets, bunkers):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    HS_clicked = play_button.rect2.collidepoint(mouse_x, mouse_y)

    if HS_clicked and not stats.game_active:
        stats.HS_active = True

    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens, alien_bullets)
        create_bunkers(ai_settings, screen, alien_bullets, bunkers)

        ship.center_ship()


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number, alien_bullets):
    alien = Alien(ai_settings, screen, alien_bullets)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens, alien_bullets):
    alien = Alien(ai_settings, screen, alien_bullets)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    ai_settings.alien_index = 0
    for row_number in range(number_rows):
        ai_settings.alien_index += 2
        if ai_settings.alien_index >= 12:
            ai_settings.alien_index = 0
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number, alien_bullets)


def create_bunker(ai_settings, screen, alien_bullets, bunker_number, bunkers):
    bunker = Bunker(ai_settings, screen, alien_bullets)
    bunker.x = 160 + 200 * bunker_number
    bunker.rect.x = bunker.x
    bunker.rect.y = 600
    bunkers.add(bunker)


def create_bunkers(ai_settings, screen, alien_bullets, bunkers):
    number_of_bunkers = 5

    for bunker_number in range(number_of_bunkers):
        create_bunker(ai_settings, screen, alien_bullets, bunker_number, bunkers)


def create_ufo(ai_settings, screen, aliens, alien_bullets):
    ai_settings.alien_index = 12
    create_alien(ai_settings, screen, aliens, -1.75, -.75, alien_bullets)


def create_ufo2(ai_settings, screen, ufo):
    ship = UFO(ai_settings, screen)
    ufo.add(ship)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo)
            break


def update_bunker(bunkers):
    bunkers.update()


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo)


def update_ufo(ai_settings, screen, ufo):
    now = pygame.time.get_ticks()

    if len(ufo) <= 0:
        if now - ai_settings.ufo_last > randint(10000, 15000):
            now = pygame.time.get_ticks()
            create_ufo2(ai_settings, screen, ufo)

    ufo.update()

    for ufo_ship in ufo.sprites():
        if ufo_ship.check_edge():
            ufo.empty()
            ai_settings.ufo_last = now
            break


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo, bunkers):
    screen_rect = screen.get_rect()

    bullets.update()
    alien_bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= screen_rect.bottom:
            alien_bullets.remove(alien_bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
    check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo)
    check_bullet_ufo_collisions(ai_settings, stats, sb, ufo, bullets)
    check_bullet_bunker_collisions(ai_settings, screen, bullets, alien_bullets, bunkers)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)

            pygame.mixer.Sound('sounds/alienCrash.wav').play()

            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens, alien_bullets)


def check_bullet_ufo_collisions(ai_settings, stats, sb, ufo, bullets):
    collisions = pygame.sprite.groupcollide(bullets, ufo, True, True)

    if collisions:
        now = pygame.time.get_ticks()
        for ufo in collisions.values():
            stats.score += ai_settings.ufo_points * len(ufo)

            pygame.mixer.Sound('sounds/alienCrash.wav').play()

            sb.prep_score()
        check_high_score(stats, sb)
        ai_settings.ufo_last = now


def check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo):
    collisions = pygame.sprite.spritecollideany(ship, alien_bullets)

    if collisions:
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo)


def check_bullet_bunker_collisions(ai_settings, screen, bullets, alien_bullets, bunkers):
    collisions = pygame.sprite.groupcollide(bullets, bunkers, True, True)
    collisions2 = pygame.sprite.groupcollide(alien_bullets, bunkers, True, True)

    if collisions or collisions2:
        ai_settings.bunker_index += 1
        create_bunkers(ai_settings, screen, alien_bullets, bunkers)
        if ai_settings.bunker_index >= 4:
            bunkers.empty()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        pygame.mixer.Sound('sounds/myLaser.wav').play()


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo):
    if stats.ships_left > 0:
        pygame.mixer.Sound('sounds/oww.wav').play()
        stats.ships_left -= 1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        ufo.empty()

        create_fleet(ai_settings, screen, ship, aliens, alien_bullets)
        ship.center_ship()

        sleep(1)

    else:
        ai_settings.alien_index = 0
        pygame.mixer.Sound('sounds/death.wav').play()
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        stats.game_active = False
        sb.check_leaderboard()
        menu.create_alien()
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


# noinspection PyPep8Naming
def display_HS_menu(screen, sb):
    screen.fill((190, 190, 190))
    sb.prep_list()
    sb.display_list()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, menu, ufo, bunkers):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    bunkers.draw(screen)

    ufo.draw(screen)

    sb.show_score()

    if not stats.game_active:
        menu.draw_menu()
        if stats.HS_active:
            display_HS_menu(screen, sb)

    pygame.display.flip()
