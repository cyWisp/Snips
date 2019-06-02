class Settings():
    # This class stores all settings for Alien Invasion

    def __init__(self):
        # Initialize all of the game's settings
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 1.5