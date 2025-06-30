nums = [1,6,120,654]
def linear_search(a):
    for i in range(len(nums)):
        if nums[i] == a:
            return i
print(linear_search(120))
def binary_search(number,start,end):
    middle = (end - start) / 2
    if nums