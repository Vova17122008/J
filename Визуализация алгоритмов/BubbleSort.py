# Пузырьковая сортировка
'''
Начнем со сравнения первых двух элементов списка. Если первый элемент больше второго, мы меняем их
местами.
Если они уже в нужном порядке, мы оставляем их как есть. Затем мы переходим к следующей паре элементов,
сравниваем их значения и меняем местами при необходимости. Этот процесс продолжается до последней пары
элементов в списке.

Достигнув конца списка, повторяем этот процесс для каждого элемента снова. Хотя это крайне неэффективно
Что если в массиве нужно сделать только одну замену? Почему мы все еще повторяем, даже если список уже
отсортирован? Получается нам нужно пройти список n^2 раза.

Очевидно, что для оптимизации алгоритма нам нужно остановить его, когда он закончит сортировку.
Откуда нам знать, что мы закончили сортировку? Если бы элементы были отсортированы, то нам не пришлось
бы их менять местами. Таким образом, всякий раз, когда мы меняем элементы, мы устанавливаем флаг
в True, чтобы повторить процесс сортировки. Если перестановок не произошло, флаг останется False, и
алгоритм остановится.
'''
import pygame
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 1000
HEIGHT = 750
FPS = 30

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
pygame.display.set_caption("BubbleSort")
clock = pygame.time.Clock()

# Создание случайных переменных
counts = 99
nums = random.sample(range(HEIGHT-100),counts)
c1 = random.sample(range(256),counts)
c2 = random.sample(range(256),counts)
c3 = random.sample(range(256),counts)
# Цикл игры
running = True
while running:


    # Обновление
    running = False
    for i in range(counts-1):
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
        if nums[i] < nums[i + 1]:
            nums[i + 1], nums[i] = nums[i], nums[i + 1]
            c1[i], c1[i+1] = c1[i+1],  c1[i]
            c2[i], c2[i + 1] = c2[i + 1], c2[i]
            c3[i], c3[i + 1] = c3[i + 1], c3[i]
            running = True
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        # После отрисовки всего, переворачиваем экран
        pygame.display.update()

pygame.quit()
def bubble_sort(nums):
    swapped = True
    k = 0
    while swapped:
        k += 1
        swapped = False
        for i in range(len(nums)-k):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
                swapped = True
a = [5, 1, 7, 3, 9, 4, 8, 2, 10]
bubble_sort(a)
print(a)