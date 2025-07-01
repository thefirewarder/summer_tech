import random
list1 = []
for i in range(500):
    list1.append(random.randint(1,1000))
def q_sort(list1, start, end):
    if start >= end:
        return

    pivot = list1[end]
    left = start
    right = end - 1

    while left <= right:
        while left <= right and list1[left] < pivot:
            left += 1
        while left <= right and list1[right] > pivot:
            right -= 1
        if left <= right:
            list1[left], list1[right] = list1[right], list1[left]
            left += 1
            right -= 1

    # Place pivot in its correct position
    list1[left], list1[end] = list1[end], list1[left]

    # Recursively sort left and right partitions
    q_sort(list1, start, left - 1)
    q_sort(list1, left + 1, end)

q_sort(list1, 0, len(list1) - 1)
print(list1)
