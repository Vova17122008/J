# Быстрая сортировка
'''
При правильной настройке он чрезвычайно эффективен и не требует дополнительного пространства памяти
как сортировка слиянием. Мы разделяем список вокруг элемента точка опоры, сортируя значения вокруг
этой точки.

Быстрая сортировка начинается с разбиения списка — выбора одного значения списка, которое будет
в его отсортированном месте. Это значение называется опорным. Все элементы, меньшие, чем этот элемент,
перемещаются влево. Все более крупные элементы перемещены вправо.
Зная, что опорный элемент находится на своем правильном месте, мы рекурсивно сортируем значения вокруг
этого элемента, пока не будет отсортирован весь список.
'''
def partition(nums, low_index, high_index):
    pivot = nums[(low_index + high_index) // 2]
    i = low_index - 1
    j = high_index + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]
def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

a = [5, 1, 7, 3, 9, 4, 8, 2, 10]
quick_sort(a)
print(a)