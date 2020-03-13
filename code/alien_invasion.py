import pygame
from pygame.sprite import Group
from setting import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200,800))

    # screen = pygame.display.set_mode(ai_settings.screen_width,
    #                                  ai_settings.screen_height)
    # 报错 是因为长宽得再一个元组中
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个用于存储外星人的编组
    aliens = Group()
    # aliens = Alien(ai_settings, screen)

    # 创建外星人
    gf.creat_fleet(ai_settings, screen, aliens, ship)

    # 创建游戏状态
    stats = GameStats(ai_settings)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            # 更新飞船状态
            ship.update()
            # 更新子弹状态
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            # 更新外星人状态
            gf.update_aliens(ai_settings, screen, stats, ship, bullets, aliens)

        # 更新屏幕
        gf.up_screen(ai_settings, screen, ship, bullets, aliens)



run_game()