# Сортировка выбором
'''
На практике нам не нужно создавать новый список для отсортированных элементов, мы будет обрабатывать
крайнюю левую часть списка как отсортированный сегмент. Затем мы ищем во всем списке наименьший элемент
и меняем его на первый элемент.

Теперь мы знаем, что первый элемент списка отсортирован, мы получаем наименьший элемент из оставшихся
элементов и заменяем его вторым элементом. Это повторяется до тех пор, пока последний элемент списка не
станет оставшимся элементом для изучения.
Этот алгоритм сегментирует список на две части: отсортированные и несортированные. Он постоянно
удаляет наименьший элемент из несортированного сегмента списка и добавляет его в отсортированный
сегмент
'''
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 1000
HEIGHT = 750
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("InsertionSort")
clock = pygame.time.Clock()

# Создание случайных переменных
counts = WIDTH // 12 - 1
nums = random.sample(range(HEIGHT-100),counts)
c1 = random.sample(range(256),counts)
c2 = random.sample(range(256),counts)
c3 = random.sample(range(256),counts)
# Цикл игры
running = True
for i in range(len(nums)):
    lowest_value_index = i
    # Обновление
    for j in range(i + 1, len(nums)):
        # Рендеринг
        screen.fill(BLACK)
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Создание столбцов
        xcor = 10
        for x in range(counts):
            # Метод для построения линии
            # c1[j]- за 1 число цвета
            # Случайный цвет- (c1[j], c2[j], c3[j])
            # Screen - экран на котором отображаем всё
            # xcor - позиция столбца по x
            # HEIGHT- позиция начальной точки по y
            # [xcor, HEIGHT]- начальные кординатые линии
            # nums[j]- случайная кордината по y от конца столбца
            # Линия отображается с самого низа [xcor, HEIGHT] до ([xcor, nums[j]]) случайной высоты
            pygame.draw.line(screen, (c1[x], c2[x], c3[x]), [xcor, HEIGHT], [xcor, nums[x]], 8)
            xcor += 12
        if nums[lowest_value_index] < nums[j]:
            lowest_value_index = j
    nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    c1[i], c1[lowest_value_index] = c1[lowest_value_index], c1[i]
    c2[i], c2[lowest_value_index] = c2[lowest_value_index], c2[i]
    c3[i], c3[lowest_value_index] = c3[lowest_value_index], c3[i]
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    # После отрисовки всего, переворачиваем экран
    pygame.display.update()
pygame.quit()

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i+1, len(nums)):
            if nums[lowest_value_index] > nums[j]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
a = [10, 5, 1, 7, 3, 9, 4, 5, 8, 2, 10, 1]
selection_sort(a)
print(a)