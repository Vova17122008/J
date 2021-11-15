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
a = random.sample(range(10000), 10000)
start = time.time()
bubble_sort(a)
finish = time.time()
print(finish - start)