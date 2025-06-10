class Setting:

    def __init__(self):
        """oyunun durağan ayarlarına ilk değer ata."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Gemi settings
        self.ship_limit = 3

        # mermi settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        #alien ayarlari
        self.fleet_drop_speed = 10


        #oyunun ne kadar çabuk hızlandığı
        self.speedup_scale = 1.1

        # uzaylı puan değerlerinin ne kadar çabuk arttığı
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """oyun boyunca değişen ayarlara ilk değer ata."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #filo yönü; 1 sağı, -1 solu temsil ediyor.
        self.fleet_direction = 1

        #skor verme
        self.alien_points = 50

    def increase_speed(self):
        """Hız ayarlarını ve uzaylı puan değerlerini arttır."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)
