import sys, pygame
from settings import Setting
from ship import Ship

class AlienInvasion:
    """
    oyunun değerlerini ve davranışını
    yönetmek için genel bir sınıf.
    """

    def __init__(self):
        """
        oyunu başlat ve
        oyun kaynaklarını oluştur.
        """
        pygame.init()
        self.settings = Setting()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height)
        )
        pygame.display.set_caption("Uzayli Istilasi")
        # Arka plan rengini ayarla.
        self.bg_color = (230, 230, 230)
        self.ship=Ship(self)

    def run_game(self):
        """Oyun için ana döngüyü başlat."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Klavye ve fare olaylarına yanıt ver."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Ekrandaki resimleri güncelle ve yeni ekran ekle."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # bir oyun örneği oluştur ve oyunu çalıştır.
    ai = AlienInvasion()
    ai.run_game()