# from sitting import Settings
class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_lim_num