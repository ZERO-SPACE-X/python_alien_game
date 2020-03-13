import pygame
from pygame.sprite import Sprite

alien_file = 'imags/alien.bmp'
class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load(alien_file)
        self.rect = self.image.get_rect()


        # 对比源代码 注释掉的
        self.screen_rect = self.screen.get_rect()
        # self.center = float(self.rect.centerx)
        # self.alien_lr_speed_factor = self.ai_settings.alien_lr_speed_factor

        # 外星人初始放置位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += self.ai_settings.alien_lr_speed_factor * self.ai_settings.direction_x
        # if self.x >= self.screen_rect.right - self.rect.width:
        #     self.ai_settings.direction_x = -1
        #     self.ai_settings.down_flag = True
        # if self.x <= 0:
        #     self.ai_settings.direction_x = 1
        #     self.ai_settings.down_flag = True

        # if self.ai_settings.down_flag == True:
        #     self.ai_settings.down_flag = False
        #     self.y += 10 * 1

        self.rect.x = self.x



    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)