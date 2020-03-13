import setting
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """初始化子弹"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.screen_rect = self.screen.get_rect()
        self.ship = ship
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor
        self.color = ai_settings.bullet_color

    # 更新子弹状态

    def update(self):
        # 当检测到空格的时候
        self.y -= self.speed_factor  # 子弹的纵坐标是在减少
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)



