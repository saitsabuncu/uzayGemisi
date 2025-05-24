import pygame.font

class Scoreboard:
    """Skor verme bilgisini bildiren sınıf. """
    def __init__(self, ai_game):
        """Skor tutan niteliklere ilk değer ata."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Skoru işlenmiş resme dönüştür."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Skoru ekrana çiz."""
        self.screen.blit(self.score_image, self.score_rect)