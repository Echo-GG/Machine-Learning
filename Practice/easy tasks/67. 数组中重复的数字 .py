# 在一个长度为n的数组里的所有数字都在0~n-1的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组[2,3,1,0,2,5,3],那么对应的输出是2或者3。存在不合法的输入的话输出-1。
list = []
arr = map(int,input("请输入数组元素: ").split())
arr = [x for x in arr]
size = len(arr)
for i in range(size):
    for j in range(i+1,size):
        if arr[i] == arr[j]:
            list.append(arr[i])
            break
if len(list) == 0:
    print(-1)
else:
    list = set(list)
    print(list)

# Another solution:
def func(nums):
    for i in nums:
        if nums.count(i) >= 2:
            return i
    return -1

print(func([1,2,4,5,5]))
print(func([1,2,3,4]))