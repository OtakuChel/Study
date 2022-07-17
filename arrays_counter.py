import random

m = int(input('Введите длину первого массива: '))
n = int(input('Введите длину первого массива: '))

nums1 = [random.randint(-1000000, 1000000) for i in range(m)]
nums2 = [random.randint(-1000000, 1000000) for i in range(n)]
nums = nums1 + nums2
nums.sort()

def calc(nums):

  if len(nums)%2 != 0:
    y = (m+n)/2
    x = nums[int(y)]
  else:
    y = (m+n)/2
    x = (nums[int(y)] + nums[int(y)-1])/2
  return f'центр массива = {x}'


print(nums1)
print(nums2)
print(nums)
print (calc(nums))