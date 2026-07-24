# 给定一个数组nums和目标值target。将target元素移动到数组前面，其他元素相对顺序不变。
def move(nums,target):
    lst = []
    count = 0
    for i in nums:
        if i != target:
            lst.append(i)
        else:
            count += 1
    res = [target for i in range(count)]
    for i in lst:
        res.append(i)
    
    return res

a = [1,1,2,1,3,4]
b = 1
print(move(a,b))

# Another solution: 
def func(nums,target):
    count = 0
    left = len(nums) - 1
    right = len(nums) - 1
    while left >= 0:
        if nums[left] != target:
            nums[right] = nums[left]
            right -= 1
        else:
            count += 1
        left -= 1
    for i in range(count):
        nums[i] = target
func(a,b)
print(a)