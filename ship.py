import pygame

class Ship:
    """Gemiyi yönetecek bir sınıf."""
    def __init__(self, ai_game):
        """
        Gemiyi başlat ve başlangıç konumunu belirle."""
        self.screen=ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        # Gemiyi yükle ve dikdörtgenini al.
        original_image = pygame.image.load('images/ship.png').convert_alpha()
        self.image = pygame.transform.scale(original_image, (60, 48))  # genişlik, yükseklik
        self.rect=self.image.get_rect()

        # Her gemiyi ekranın alt merkezinde başlat.
        self.rect.midbottom=self.screen_rect.midbottom

        #geminn yatay ve dikey konumları için ondalık değeri sakla
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Hareket bayrakları
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """
        hareket bayrağına bağlı olarak
        konumu güncelle
        """
        # rect'i değil de geminin x, y değerini güncelle
        # Sağ/sol hareket
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Yukarı/aşağı hareket
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Gemiyi mevcut konumunda çiz."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """gemiyi ekrandan merkeze koy."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)