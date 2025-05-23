class Setting:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # Gemi settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # mermi settings
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 4
        #alien ayarlari
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #filo yönü; 1 sağı, -1 solu temsil ediyor.
        self.fleet_direction = 1
