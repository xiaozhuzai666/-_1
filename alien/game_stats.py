class GameStats():
    """跟着游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的数据"""
        self.ship_left = self.ai_settings.ship_limit