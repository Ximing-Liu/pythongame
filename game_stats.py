class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.ships_left = self.ai_settings.ship_limit

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
