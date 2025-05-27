import sys, pygame
from time import sleep
from settings import Setting
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """
    oyunun değerlerini ve davranışını
    yönetmek için genel bir sınıf.
    """

    def __init__(self):
        """oyunu başlat ve oyun kaynaklarını oluştur.
        """
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))

        pygame.display.set_caption("Uzayli Istilasi")
        # bir skorbord ve Oyun istatistiklerini saklamak
        # bir örnek oluştur.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        # Arka plan rengini ayarla.
        self.bg_color = (230, 230, 230)
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Play düğmesini oluştur.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Oyun için ana döngüyü başlat."""
        try:
            while True:
                self._check_events()

                if self.stats.game_active:
                    self.ship.update()
                    self._update_bullets()
                    self._update_aliens()

                self._update_screen()
        finally:
            self.stats.save_high_score()

    def _check_events(self):
        """Klavye ve fare olaylarına yanıt ver."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                    #self.ship.rect.x += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Oyuncu Play'e tıkladığında yeni bir oyun başlat."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # oyun ayarlarını resetle.
            self.settings.initialize_dynamic_settings()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self._start_game()

    def _check_keydown_events(self,event):
        """tuşa basmalara yanıt ver."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self._start_game()

    def _start_game(self):
        """Yeni bir oyun başlat."""
        self.stats.reset_stats()
        self.stats.game_active = True
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
        # Fare imlecini gizle.
        pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event):
        """Tuşu serbest bırakmalara yanıt ver."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """yeni bir mermi oluştur
        ve bu mermi grubunu sakla,
        Gemiden birden fazla yerden mermi ateşle.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            # Orta mermi
            center_bullet = Bullet(self)
            center_bullet.rect.midtop = self.ship.rect.midtop
            center_bullet.y = float(center_bullet.rect.y)
            self.bullets.add(center_bullet)

            # Sol mermi
            left_bullet = Bullet(self)
            left_bullet.rect.midtop = self.ship.rect.midleft
            left_bullet.rect.x -= 5  # Biraz sola kaydır
            left_bullet.y = float(left_bullet.rect.y)
            self.bullets.add(left_bullet)

            # Sağ mermi
            right_bullet = Bullet(self)
            right_bullet.rect.midtop = self.ship.rect.midright
            right_bullet.rect.x += 15  # Biraz sağa kaydır
            right_bullet.y = float(right_bullet.rect.y)
            self.bullets.add(right_bullet)

    def _update_bullets(self):
        """mermilerin konumunu güncelle ve
        eski mermilerden kurtul."""
        self.bullets.update()
        # kaybolan mermilerden kurtul.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #uzaylılara çarpan mermileri kontrol et.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """mermi-uzaylı çarpışmasına yanıt ver."""
        # çarpışan mermi ve uzaylıları sil.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # var olan mermileri imha et ve yeni filo oluştur.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # print("Yeni uzaylı sayısı:", len(self.aliens))
            # seviyeyi arttır.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Filonun kenarda olup olmadığını
        kontrol et , daha sonra filodaki tüm
        uzaylıların konumunu güncelle
        ve ve çarpışmayı kontrol et."""
        self._check_fleet_edges()
        self.aliens.update()

        # Uzaylı-gemi çarpışmasını kontrol et
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # ekranın alt tarafına çarpan uzaylıları ara.
        self._check_aliens_bottom()

    def _update_screen(self):
        """Ekrandaki resimleri güncelle ve yeni ekran ekle."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # skor bilgisini çiz.
        self.sb.show_score()

        # Oyun aktif değilse play düğmesini çiz.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """uzaylı filosunu oluştur."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Ekrana sığan uzaylı satırları sayısını belirle.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)
        # tüm uzaylı filosunu oluştur.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """bir uzaylı oluştur ve satıra yerleştir. """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        herhangi bir uzaylı bir kenara
        ulaştığında uygun bir şekilde yanıt ver.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """tüm bir filoyu düşür
        ve filonun yönünü değiştir."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """uzaylı tarafından vurulan gemiye yanıt ver."""
        if self.stats.ships_left > 0:
            # ship_left'i azalt ve skorbordu güncelle.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

        # geri kalan uzaylı ve mermilerden kurtul.
            self.aliens.empty()
            self.bullets.empty()

        # yeni bir filo oluştur ve gemiyi merkeze koy.
            self._create_fleet()
            self.ship.center_ship()
        # durdur
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """ Herhangi bir uzaylının ekranın alt
        tarafına ulaşıp ulaşmadığını kontrol et."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #buna gemiye çarpıldığında olduğu gibi muamele et.
                self._ship_hit()
                break

if __name__ == '__main__':
    # bir oyun örneği oluştur ve oyunu çalıştır.
    ai = AlienInvasion()
    ai.run_game()