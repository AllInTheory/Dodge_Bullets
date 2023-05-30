import pygame
import math
import random
import sys
import time

# 初始化Pygame
pygame.init()

# 定义屏幕尺寸
width, height = 1200, 800

# 创建游戏窗口
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge Bullets")

# 加载对象图片
object_image = pygame.image.load('images/ufo.webp')

# 加载背景图片
background_image = pygame.image.load("images/back.webp")
background_image = pygame.transform.scale(background_image, (1200, 800))

# 缩放对象图片
new_width = 80
new_height = 60
object_image = pygame.transform.scale(object_image, (new_width, new_height))

# 获取图片的宽度和高度
object_width = object_image.get_width()
object_height = object_image.get_height()

# 设置对象初始位置为屏幕中心
object_x = (width - object_width) // 2
object_y = (height - object_height) // 2

# 目标位置和移动速度
target_x = object_x
target_y = object_y
move_speed = 2
normal_move_speed = move_speed  # 默认移动速度
fast_move_speed = 5  # 快速移动速度
deceleration_rate = 0.01  # 减速率

# 创建对象精灵
object_sprite = pygame.sprite.Sprite()
object_sprite.image = object_image
object_sprite.rect = object_sprite.image.get_rect()
object_sprite.rect.x = object_x
object_sprite.rect.y = object_y

# 创建字体对象
font = pygame.font.Font(None, 36)

# 创建文本表面
text_lines = [
    "Press 'S' To Start.",
    "Use the right mouse button to control the movement of the spaceship.",
    "Press 'D' to speed up.",
    "Press 'F' to flash to mouse position",
    "You only have 5 HP"
]
text_surfaces = []
for line in text_lines:
    text_surface = font.render(line, True, (255, 250, 250))
    text_surfaces.append(text_surface)

# 设置文本位置
text_rects = []
for i, surface in enumerate(text_surfaces):
    rect = surface.get_rect()
    rect.center = (width // 2, height // 2 + (i - len(text_lines) // 2) * 40)
    text_rects.append(rect)

# 等待用户按下 's' 键开始游戏
start_game = False
started = False
start_time = 0
end_time = 0
while not start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and not started:
            start_game = True
            started = True
            start_time = time.time()

    screen.blit(background_image, (0, 0))
    for surface, rect in zip(text_surfaces, text_rects):
        screen.blit(surface, rect)
    pygame.display.flip()

bullet_count = 6


# 定义子弹1类
class Bullet1(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((15, 3))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > width:  # 子弹1到达屏幕右边缘时消失并重新生成
            self.rect.x = 0
            self.rect.y = random.randint(0, height)


# 创建子弹1编组
bullets1 = pygame.sprite.Group()

# 生成x个子弹1对象，并添加到编组中
for _ in range(bullet_count):
    bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
    bullet = Bullet1(0, random.randint(0, height), bullet_speed)
    bullets1.add(bullet)


# 定义子弹2类
class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:  # 子弹2到达屏幕下边缘时消失并重新生成
            self.rect.y = 0
            self.rect.x = random.randint(0, width)


# 创建子弹2编组
bullets2 = pygame.sprite.Group()

# 生成x个子弹2对象，并添加到编组中
for _ in range(bullet_count):
    bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
    bullet = Bullet2(random.randint(0, width), 0, bullet_speed)
    bullets2.add(bullet)


# 定义子弹3类
class Bullet3(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((15, 3))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:  # 子弹3到达屏幕左边缘时消失并重新生成
            self.rect.x = width
            self.rect.y = random.randint(0, height)


# 创建子弹3编组
bullets3 = pygame.sprite.Group()

# 生成x个子弹3对象，并添加到编组中
for _ in range(bullet_count):
    bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
    bullet = Bullet3(width, random.randint(0, height), bullet_speed)
    bullets3.add(bullet)


# 定义子弹4类
class Bullet4(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0:  # 子弹4到达屏幕上边缘时消失并重新生成
            self.rect.y = height
            self.rect.x = random.randint(0, width)


# 创建子弹4编组
bullets4 = pygame.sprite.Group()

# 生成x个子弹4对象，并添加到编组中
for _ in range(bullet_count):
    bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
    bullet = Bullet4(random.randint(0, width), height, bullet_speed)
    bullets4.add(bullet)

# 定义对象血量
object_health = 5

# 定义响应次数的初始值
max_keypresses_d = 3
keypresses_remaining_d = max_keypresses_d
max_keypresses_f = 3
keypresses_remaining_f = max_keypresses_f

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 鼠标右键点击事件
            # 获取鼠标点击位置
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 设置新的目标位置
            target_x = mouse_x - object_width // 2
            target_y = mouse_y - object_height // 2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # 按下D键
                if keypresses_remaining_d > 0:
                    move_speed = fast_move_speed
                    keypresses_remaining_d -= 1
            elif event.key == pygame.K_f:  # 按下F键
                if keypresses_remaining_f > 0:
                    # 获取光标位置
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # 移动至光标位置
                    object_x = mouse_x - object_width // 2
                    object_y = mouse_y - object_height // 2
                    target_x = object_x
                    target_y = object_y
                    move_speed = normal_move_speed
                    keypresses_remaining_f -= 1

    # 计算对象移动的向量
    dx = target_x - object_x
    dy = target_y - object_y

    # 计算对象当前帧的移动距离
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance > move_speed:
        direction_x = dx / distance
        direction_y = dy / distance
        move_x = direction_x * move_speed
        move_y = direction_y * move_speed
    else:
        move_x = dx
        move_y = dy

    # 更新对象位置
    object_x += move_x
    object_y += move_y

    # 判断是否需要减速
    if move_speed > normal_move_speed:
        move_speed -= deceleration_rate

    # 更新子弹1位置并检测碰撞
    bullets1.update()
    for bullet in bullets1:
        if bullet.rect.colliderect(object_sprite.rect):
            bullet.rect.x = 0  # 将子弹1的位置重置为初始位置
            bullet.rect.y = random.randint(0, height)
            bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
            object_health -= 1
            if object_health == 0:
                game_over = True

    # 更新子弹2位置并检测碰撞
    bullets2.update()
    for bullet in bullets2:
        if bullet.rect.colliderect(object_sprite.rect):
            bullet.rect.y = 0  # 将子弹2的位置重置为初始位置
            bullet.rect.x = random.randint(0, width)
            bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
            object_health -= 1
            if object_health == 0:
                game_over = True

    # 更新子弹3位置并检测碰撞
    bullets3.update()
    for bullet in bullets3:
        if bullet.rect.colliderect(object_sprite.rect):
            bullet.rect.x = width  # 将子弹3的位置重置为初始位置
            bullet.rect.y = random.randint(0, height)
            bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
            object_health -= 1
            if object_health == 0:
                game_over = True

    # 更新子弹4位置并检测碰撞
    bullets4.update()
    for bullet in bullets4:
        if bullet.rect.colliderect(object_sprite.rect):
            bullet.rect.y = height  # 将子弹4的位置重置为初始位置
            bullet.rect.x = random.randint(0, width)
            bullet_speed = random.uniform(0.5, 3)  # 随机生成速度值
            object_health -= 1
            if object_health == 0:
                game_over = True

    # 更新对象精灵的rect属性
    object_sprite.rect.x = object_x
    object_sprite.rect.y = object_y

    # 绘制游戏界面
    screen.blit(background_image, (0, 0))
    screen.blit(object_image, (object_x, object_y))  # 绘制对象
    font = pygame.font.Font(None, 36)
    text_d = font.render(f"D Speed_Up: {keypresses_remaining_d}", True, (255, 250, 250))
    text_f = font.render(f"F Flash: {keypresses_remaining_f}", True, (255, 250, 250))
    screen.blit(text_d, (0, 0))
    screen.blit(text_f, (0, 40))  # 绘制剩余响应次数

    # 绘制血量文本
    font = pygame.font.Font(None, 36)
    text = font.render("Health: " + str(object_health), True, (255, 250, 250))
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height - 50)
    screen.blit(text, text_rect)

    # 绘制子弹1
    for bullet1 in bullets1:
        screen.blit(bullet1.image, bullet1.rect)

    # 绘制子弹2
    for bullet2 in bullets2:
        screen.blit(bullet2.image, bullet2.rect)

    # 绘制子弹3
    for bullet3 in bullets3:
        screen.blit(bullet3.image, bullet3.rect)

    # 绘制子弹4
    for bullet4 in bullets4:
        screen.blit(bullet4.image, bullet4.rect)

    if object_health == 0:
        game_over = True
        running = False
        end_time = time.time()

    if not started:
        for surface, rect in zip(text_surfaces, text_rects):
            screen.blit(surface, rect)
    elif end_time == 0:
        current_time = time.time()
        elapsed_time = current_time - start_time
        time_text = f"Time: {elapsed_time:.2f}s"
        time_surface = font.render(time_text, True, (255, 250, 250))
        time_rect = time_surface.get_rect()
        time_rect.center = (width // 2, 30)
        screen.blit(time_surface, time_rect)

    pygame.display.flip()

    # 限制游戏帧率
    clock.tick(120)

# 游戏结束
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game_over = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and started:
            running = False
            game_over = False

    screen.blit(background_image, (0, 0))
    end_text = font.render("Press 'E' To End this game.", True, (255, 250, 250))
    end_text_rect = end_text.get_rect()
    end_text_rect.center = (width // 2, height // 2)
    screen.blit(end_text, end_text_rect)
    total_time = end_time - start_time
    time_text = f"Total Time: {total_time:.2f}s"
    time_surface = font.render(time_text, True, (255, 250, 250))
    time_rect = time_surface.get_rect()
    time_rect.center = (width // 2, 30)
    screen.blit(time_surface, time_rect)
    pygame.display.flip()

# 退出游戏
pygame.quit()
sys.exit()
