import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Filodaki tek uzaylıyı temsil eder."""
    def __init__(self, ai_game):
        """uzaylıyı başlat ve
        başlangıç konumunu belirle."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #uzaylı resmini yükle ve rect niteliğini ayarla.
        original_image = pygame.image.load('images/alien.png').convert_alpha()
        self.image = pygame.transform.scale(original_image, (60, 48))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """uzaylı ekranın kenarında ise True döndürür."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """uzaylıyı sağa veya sola hareket ettir."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x