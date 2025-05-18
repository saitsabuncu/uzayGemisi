import sys, pygame
from settings import Setting

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

    def run_game(self):
        """Oyun için ana döngüyü başlat."""
        while True:
            # Klavye ve fare olaylarını gözle.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Döngüden her geçişte ekranı yeniden çizdir.
            self.screen.fill(self.settings.bg_color)
            # En son çizilen ekranı görünür yap.
            pygame.display.flip()

if __name__ == '__main__':
    # bir oyun örneği oluştur ve oyunu çalıştır.
    ai = AlienInvasion()
    ai.run_game()