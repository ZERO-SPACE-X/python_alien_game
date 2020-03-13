import sys
import pygame
from setting import Settings
from bullet import Bullet
from alien import Alien
from ship import Ship

def check_keydown_event(event, ai_settings, screen, ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 这里可以使用elif是因为每个按键都
        # 会出发一个事件，相当于这个这个for循环会进入两次，如果左右键一起按，会
        # 检测一次右键再检测一次左键，这样两个标志位都会变成True 而不会只检测到
        # 一个
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):

    for event in pygame.event.get():    # 每按一次按键，就会进入一次这个for循环
        # 感觉这个event.get是一个列表，会把所有的事件放在一个列表中，然后依次处理。
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def fire_bullets(bullets, ai_settings, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    bullets.update()
    # 删除已消失的子弹
    # 在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本。我们使用了方法
    # copy()来设置for循环，这让我们能够在循环中修改bullets 。我们检查每颗子弹，看看
    # 它是否已从屏幕顶端消失。如果是这样，就将其从bullets中删除，我们使用了一条print
    # 语句，以显示当前还有多少颗子弹， 从而核实已消失的子弹确实删除了。

    # 为什么是遍历的副本，直接遍历编组，然后删除编组中屏幕外的子弹不好吗？？
    # for bullet in bullets:

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) # 调试使用，实际运行时节约资源，将此语句注释掉
    check_bullet_alien_collsions(ai_settings, screen, ship, bullets, aliens)

def check_bullet_alien_collsions(ai_settings, screen, ship, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True) # False 表示子弹在发生碰撞之后不消失，改成True 子弹就消失了
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(ai_settings, screen, aliens, ship)


def get_number_aliens_x(ai_settings, alien_width):
    allow_space_x = ai_settings.screen_width - 2 * alien_width
    each_row_alien_num = allow_space_x // (alien_width * 2)
    return each_row_alien_num

# 通过不同的坐标绘制图片，当需要循环时，需要对X Y的坐标分别做计算，这样才能绘制出好几行图片
def creat_alien(ai_settings, screen, aliens, alien_number,alien_row):
    new_alien = Alien(ai_settings, screen)
    new_alien_width = new_alien.rect.width
    new_alien.x = new_alien_width + new_alien_width * 2 * alien_number
    new_alien.y = new_alien.rect.height + new_alien.rect.height * 2 * alien_row
    new_alien.rect.x = new_alien.x
    new_alien.rect.y = new_alien.y
    aliens.add(new_alien)


def get_number_rows(ai_settings, ship, alien_height):
    allowed_height = ai_settings.screen_height - ship.rect.height - 3 * alien_height
    number_rows = allowed_height // (alien_height * 2)
    return number_rows


def creat_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    alien_width = alien.rect.width
    for alien_row in range(get_number_rows(ai_settings, ship, alien_height)):
        for alien_number in range(get_number_aliens_x(ai_settings, alien_width)):
            creat_alien(ai_settings, screen, aliens, alien_number, alien_row)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_directions(ai_settings, aliens)
            break


def change_alien_directions(ai_settings, aliens):
    ai_settings.direction_x *= -1
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.drop_speed


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def up_screen(ai_settings, screen, ship, bullets, aliens):
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    ship.blitme()

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制外星人
    # for alien in aliens.sprites():
    #     alien.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()