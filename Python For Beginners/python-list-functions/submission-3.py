from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sumosa = 0
    for i in nums:
        sumosa += i
    return sumosa

def get_min(nums: List[int]) -> int:
    minmosa = nums[0]
    for num in nums:
        if num < minmosa:
            minmosa = num
    return minmosa

def get_max(nums: List[int]) -> int:
    maxmosa = nums[0]
    
    for i in nums:
        if i > maxmosa:
            maxmosa = i
    return maxmosa
    

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
