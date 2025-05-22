import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Filodaki tek uzaylıyı temsil eder."""
    def __init__(self, ai_game):
        """uzaylıyı başlat ve
        başlangıç konumunu belirle."""
        super().__init__()
        self.screen = ai_game.screen

        #uzaylı resmini yükle ve rect niteliğini ayarla.
        original_image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(original_image, (60, 48))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)