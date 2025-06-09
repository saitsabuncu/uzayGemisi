class GameStats:
    """Uzaylı İstilası için istatistikleri takip eder."""

    def __init__(self, ai_game):
        """İstatistikleri başlat."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Oyun başlangıçta aktif değil
        self.game_active = False

        # Kalıcı yüksek skoru yükle
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Oyun sırasında değişebilecek istatistikleri sıfırla."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        """Dosyadan yüksek skoru yükle."""
        try:
            with open('high_score.txt', 'r', encoding='utf-8') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Yüksek skoru dosyaya kaydet."""
        with open('high_score.txt', 'w', encoding='utf-8') as f:
            f.write(str(self.high_score))
