import pygame
import sys

class Settings():
    """创建一个设置类"""
    def __init__(self):
        self.bg_color = (230,230,230)  # 灰色背景
        # self.bg_color = (255, 255, 255) # 白色背景
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed_factor = 1.5

        # 子弹参数设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 设置外星人的参数
        self.alien_lr_speed_factor = 1
        self.direction_x = 1
        self.drop_speed = 10
        self.down_flag = False