import sys, pygame
from settings import Setting
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
        self.screen = pygame.display.set_mode((0, 0),
                                              pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Uzayli Istilasi")
        # Arka plan rengini ayarla.
        self.bg_color = (230, 230, 230)
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Oyun için ana döngüyü başlat."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            #print(len(self.bullets))

            self._update_screen()

    def _check_events(self):
        """Klavye ve fare olaylarına yanıt ver."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    #Gemiyi sağa hareket ettir.
                    #self.ship.rect.x += 1

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
        ve bu mermi grubunu sakla."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """mermilerin konumu update ve
        mermilerden kurtul."""
        self.bullets.update()
        # kaybolan mermilerden kurtul.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Ekrandaki resimleri güncelle ve yeni ekran ekle."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Önce tüm mermileri çiz
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Sonra uzaylıları bir kez çiz
        self.aliens.draw(self.screen)

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
if __name__ == '__main__':
    # bir oyun örneği oluştur ve oyunu çalıştır.
    ai = AlienInvasion()
    ai.run_game()