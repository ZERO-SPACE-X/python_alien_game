# from sitting import Settings
class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = True
        self.restart()

    def restart(self):
        self.ship_left = self.ai_settings.ship_lim_num