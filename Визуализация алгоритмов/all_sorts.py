from copy import deepcopy
import random
import time

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




def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i+1, len(nums)):
            if nums[lowest_value_index] > nums[j]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


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

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        left_index = i-1
        while left_index >= 0 and nums[left_index] > item_to_insert:
            nums[left_index+1] = nums[left_index]
            left_index -= 1
        nums[left_index+1] = item_to_insert

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

original = random.sample(range(10000), 10000)
print("Сортировка 10.000 элементов")
copy = deepcopy(original)
start = time.time()
selection_sort(copy)
finish = time.time()
print(finish - start, "Сортировка выбором")

copy = deepcopy(original)
start = time.time()
bubble_sort(copy)
finish = time.time()
print(finish - start, "Пузырьковая сортировка")

copy = deepcopy(original)
start = time.time()
quick_sort(copy)
finish = time.time()
print(finish - start, "Быстрая сортировка")

copy = deepcopy(original)
start = time.time()
insertion_sort(copy)
finish = time.time()
print(finish - start, "Сортировка вставками")

copy = deepcopy(original)
start = time.time()
heap_sort(copy)
finish = time.time()
print(finish - start, "Сортировка кучей")

copy = deepcopy(original)
start = time.time()
copy.sort()
finish = time.time()
print(finish - start, "Стандартная сортировка")
