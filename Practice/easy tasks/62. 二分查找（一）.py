# 请实现无重复数字的升序数组的二分查找
# 给定一个元素升序的、无重复数字的整型数组nums和一个目标值target，写一个函数搜索nums中的target，
# 如果目标值存在返回下标（下标从0开始），否则返回-1

def binary_search(nums,target):
    l = 0
    r = len(nums) - 1
    while(l<=r):
        pivot = l + (r-l) // 2
        if target < nums[pivot]:
            r = pivot - 1
        elif target > nums[pivot]:
            l = pivot + 1
        else:
            return pivot
    return -1
    
arr = [-1,3,4,7,9,10,100,210,302]
print(arr)

target = int(input("请输入要查找的值: "))
print(binary_search(arr,target))