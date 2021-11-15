# Сортировка вставками
'''
Как и Сортировка выбором, этот алгоритм сегментирует список на отсортированные и несортированные части.
Он перебирает несортированный сегмент и вставляет просматриваемый элемент в правильную позицию
отсортированного списка.

Предполагается, что первый элемент списка отсортирован. Затем мы переходим к следующему элементу,
назовем его х. Если x больше первого элемента, мы оставляем его как есть. Если x меньше, мы копируем
значение первого элемента во вторую позицию и затем устанавливаем первый элемент в x.

Когда мы переходим к другим элементам несортированного сегмента, мы непрерывно перемещаем более крупные
элементы в отсортированном сегменте вверх по списку, пока не встретим элемент меньше x,
или не достигнем конца отсортированного сегмента, а затем поместим x в его правильное положение.
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
counts = 90
nums = random.sample(range(HEIGHT-100),counts)
c1 = random.sample(range(256),counts)
c2 = random.sample(range(256),counts)
c3 = random.sample(range(256),counts)
# Цикл игры
running = True
for i in range(1, len(nums)):
    item_to_insert = nums[i]
    c1_to_insert = c1[i]
    c2_to_insert = c2[i]
    c3_to_insert = c3[i]
    left_index = i - 1
    # Обновление
    while left_index >= 0 and nums[left_index] < item_to_insert:
        # Рендеринг
        screen.fill(BLACK)
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Создание столбцов
        xcor = 10
        for j in range(counts):
            # Метод для построения линии
            # c1[j]- за 1 число цвета
            # Случайный цвет- (c1[j], c2[j], c3[j])
            # Screen - экран на котором отображаем всё
            # xcor - позиция столбца по x
            # HEIGHT- позиция начальной точки по y
            # [xcor, HEIGHT]- начальные кординатые линии
            # nums[j]- случайная кордината по y от конца столбца
            # Линия отображается с самого низа [xcor, HEIGHT] до ([xcor, nums[j]]) случайной высоты
            pygame.draw.line(screen, (c1[j], c2[j], c3[j]), [xcor, HEIGHT], [xcor, nums[j]], 4)
            xcor += 10
        nums[left_index+1] = nums[left_index]
        c1[left_index+1] = c1[left_index]
        c2[left_index + 1] = c2[left_index]
        c3[left_index + 1] = c3[left_index]
        left_index -= 1
    nums[left_index+1] = item_to_insert
    c1[left_index + 1] = c1_to_insert
    c2[left_index + 1] = c2_to_insert
    c3[left_index + 1] = c3_to_insert
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    # После отрисовки всего, переворачиваем экран
    pygame.display.update()
pygame.quit()

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        left_index = i-1
        while left_index >= 0 and nums[left_index] > item_to_insert:
            nums[left_index+1] = nums[left_index]
            left_index -= 1
        nums[left_index+1] = item_to_insert
a = [5, 1, 7, 3, 9, 4, 8, 2, 10]
insertion_sort(a)
print(a)
