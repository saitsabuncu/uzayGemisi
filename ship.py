import pygame

class Ship:
    """Gemiyi yönetecek bir sınıf."""
    def __init__(self, ai_game):
        """
        Gemiyi başlat ve başlangıç konumunu belirle."""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        # Gemiyi yükle ve dikdörtgenini al.
        original_image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(original_image, (60, 48))  # genişlik, yükseklik
        self.rect=self.image.get_rect()

        # Her gemiyi ekranın alt merkezinde başlat.
        self.rect.midbottom=self.screen_rect.midbottom

        #Hareket bayrağı
        self.moving_right = False

    def update(self):
        """ geminin konumunu güncelle """
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Gemiyi mevcut konumunda çiz."""
        self.screen.blit(self.image, self.rect)