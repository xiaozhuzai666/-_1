import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    #初始化pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Ainen Invasion")
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于储存子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()
    #创造外星人
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #统计一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)
    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")



    #开始游戏的主循环
    while True:
        #管理事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)

        if stats.game_active:
           ship.update()
           gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
           gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)


run_game()