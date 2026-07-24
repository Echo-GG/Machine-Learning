# 请实现有重复数字的升序数组的二分查找
# 给定一个元素有序的（升序）长度为n的整型数组nums和一个目标值target，写一个函数搜索nums中的第一个出现的target，
# 如果目标值存在返回下标，否则返回-1

def binary_search(nums,target):
    l = 0
    r = len(nums) - 1
    while(l<=r):
        pivot = l + (r-l)//2
        if target == nums[pivot]:
            temp = pivot
            while(temp >= 0 and target == nums[temp]):
                temp -= 1
            return temp + 1
        elif target < nums[pivot]:
            r = pivot - 1
        else:
            l = pivot + 1
    return -1

target = int(input("请输入要查找的值: "))
arr = [3,3,3,4,5]
print(binary_search(arr,target))
