import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Название окна и иконка
pygame.display.set_caption('Shooting Game')
icon = pygame.image.load("img/1.jpg")
pygame.display.set_icon(icon)

# Загружаем изображение цели
target_img = pygame.image.load("img/a.png")
target_width = 80
target_height = 80

# Начальные координаты цели и скорость движения
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-3, 3])  # Скорость по X
target_speed_y = random.choice([-3, 3])  # Скорость по Y

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Шрифт для отображения очков
font = pygame.font.Font(None, 36)

# Очки игрока
score = 0

# Основной цикл игры
running = True
while running:
    screen.fill(color)  # Заливаем экран случайным цветом

    # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на выход за пределы экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x *= -1  # Меняем направление по X
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y *= -1  # Меняем направление по Y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получаем координаты мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем попадание в цель
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещаем цель на новое случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Меняем цвет фона
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Увеличиваем очки
                score += 1

    # Отображаем мишень
    screen.blit(target_img, (target_x, target_y))

    # Отображаем количество очков
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновляем экран
    pygame.display.update()

# Завершаем Pygame
pygame.quit()
