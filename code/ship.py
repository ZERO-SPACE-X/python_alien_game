import pygame
import setting
# image_file = 'images//plane.bmp'
image_file = 'images/ship.bmp'

class Ship():
    """飞船相关的初始化"""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        """load ship bmp and location"""
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings


        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        # 再center变量中存储飞船位置坐标的小数值
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:    # 此处不能用elif 因为那样每次都先检测RIGHT，如果
            # 左右键同时按下的话，将只能检测到右键的动作，这样当两个键同时按下的时候
            # 就只会向右移动，而不是原地不动
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象,centerx这个变量只能存储整数，但是不影响，因为在
        # 每次进行小数叠加的时候就已经提高了精度

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
