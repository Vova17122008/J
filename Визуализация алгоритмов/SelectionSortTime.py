import random
import time
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i+1, len(nums)):
            if nums[lowest_value_index] > nums[j]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
a = random.sample(range(10000), 10000)
start = time.time()
selection_sort(a)
finish = time.time()
print(finish - start)