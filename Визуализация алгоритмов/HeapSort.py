# Сортировка кучей
# Пирамидальная сортировка
'''
Этот популярный алгоритм сортировки, как сортировки вставками и выбором, сегментирует список
на отсортированные и несортированные части. Он преобразует несортированный сегмент списка в структуру
данных типа куча (heap), чтобы мы могли эффективно определить самый большой элемент.

Мы начинаем с преобразования списка в Max Heap — бинарное дерево, где самым большим элементом
является корневой узел. Затем мы помещаем этот элемент в конец списка. Затем мы восстанавливаем
нашу Max Heap, которая теперь имеет на одно меньшее значение, помещая новое наибольшее значение
перед последним элементом списка.
Мы повторяем этот процесс построения кучи, пока все узлы не будут удалены.
'''

# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

def heapify(root_index, heap_size, nums, c1, c2, c3):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    if left_child < heap_size and nums[left_child] < nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] < nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[largest], nums[root_index] = nums[root_index], nums[largest]
        c1[largest], c1[root_index] = c1[root_index], c1[largest]
        c2[largest], c2[root_index] = c2[root_index], c2[largest]
        c3[largest], c3[root_index] = c3[root_index], c3[largest]
        heapify(largest, heap_size, nums, c1, c2, c3)

WIDTH = 1000
HEIGHT = 750
FPS = 1

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

nums_counts = len(nums)
for i in range(nums_counts, -1, -1):
    heapify(i, nums_counts, nums, c1, c2, c3)

# Цикл игры
running = True
for i in range(nums_counts - 1, 0, -1):
    # Обновление

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

    nums[0], nums[i] = nums[i], nums[0]
    c1[0], c1[i] = c1[i], c1[0]
    c2[i], c2[0] = c2[0], c2[i]
    c3[0], c3[i] = c3[i], c3[0]
    heapify(0, i, nums, c1, c2, c3)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    # После отрисовки всего, переворачиваем экран
    pygame.display.update()
pygame.quit()

def heapify(root_index, heap_size, nums):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[largest], nums[root_index] = nums[root_index], nums[largest]
        heapify(largest, heap_size, nums)

def heap_sort(nums):
    nums_counts = len(nums)
    for i in range(nums_counts, -1, -1):
        heapify(i, nums_counts, nums)
    for i in range(nums_counts - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(0, i, nums)

a = [5, 1, 7, 3, 9, 4, 8, 2, 10]
heap_sort(a)
print(a)