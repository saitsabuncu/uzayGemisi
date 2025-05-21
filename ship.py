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

        # Hareket bayrakları
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Sağ/sol hareket
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        # Yukarı/aşağı hareket
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        """Gemiyi mevcut konumunda çiz."""
        self.screen.blit(self.image, self.rect)