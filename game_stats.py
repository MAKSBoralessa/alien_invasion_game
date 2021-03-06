class GameStats():
    """Track stats for Alien Invasion"""
    
    def __init__(self, ai_settings):
        """Initialize stats."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #Start Alien Invasion in an active state.
        self.game_active = True
        
    def reset_stats(self):
        """Initialize stats that can change during game"""
        self.ships_left = self.ai_settings.ship_limit
