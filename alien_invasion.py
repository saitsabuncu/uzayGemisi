import sys, pygame

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
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Uzayli Istilasi")

    def run_game(self):
        """Oyun için ana döngüyü başlat."""
        while True:
            # Klavye ve fare olaylarını gözle.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # En son çizilen ekranı görünür yap.
            pygame.display.flip()

if __name__ == '__main__':
    # bir oyun örneği oluştur ve oyunu çalıştır.
    ai = AlienInvasion()
    ai.run_game()