class GameStats:
    """Uzaylı istilası için istatistik tut."""
    def __init__(self, ai_game):
        """istatistiklere ilk değer ata."""
        self.settings = ai_game.settings
        self.reset_stats()

        # oyunu aktif olmayan durumda başlat.
        self.game_active = False

    def reset_stats(self):
        """oyun esnasında değişebilecek
        istatistiklere ilk değer ata."""
        self.ships_left = self.settings.ship_limit