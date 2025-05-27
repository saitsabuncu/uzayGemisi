class GameStats:
    """Uzaylı istilası için istatistik tut."""
    def __init__(self, ai_game):
        """istatistiklere ilk değer ata."""
        self.settings = ai_game.settings
        self.reset_stats()

        # oyunu aktif olmayan durumda başlat.
        self.game_active = False

        # yüksek skoru dosyadan yükle
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """oyun esnasında değişebilecek
        istatistiklere ilk değer ata."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Dosyadan yüksek skoru yükle."""
        try:
            with open('high_score.txt') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Yüksek skoru dosyaya kaydet."""
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))