class GameStats:
    """Uzaylı istilası için istatistik tut."""
    def __init__(self, ai_game):
        """istatistiklere ilk değer ata."""
        self.settings = ai_game.settings
        self.reset_stats()

        # oyunu aktif olmayan durumda başlat.
        self.game_active = False

        # en yüksek skor hiçbir zaman resetlenmemeli.
        self.high_score = 0

    def reset_stats(self):
        """oyun esnasında değişebilecek
        istatistiklere ilk değer ata."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1