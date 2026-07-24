# 给定一个数组，请实现将所有0移动到数组末尾并且不改变其他数字的相对顺序
arr = [0,3,0,2,3,0,0,1,8]

# Method 1: 
for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(0)
print(arr)

# Method 2: 
cnt = 0

list = []
for i in arr:
    if i != 0:
        list.append(i)
    else:
        cnt += 1
for i in range(cnt):
    list.append(0)
print(list)

# Method 3 :

size = len(arr)
i = 0
while i < size:
    if arr[i] == 0:
        arr.remove(arr[i])
        size = len(arr)   # ← 重新绑定，下次条件会重算
    else:
        i += 1
for j in range(i-1): # Attention!
    arr.append(0)
print(arr)

# Failed Method : 
# range 是对当前数组的一个快照，一经创建大小就固定了，不会再被修改。
# 想修改应当使用 Method 3 中的while 方法，因为 while 每次循环都会重新计算条件
# size = len(arr)
# for i in range(0,size):
#     if arr[i] == 0: # Index Error!
#         arr.remove(arr[i])
#         cnt += 1
#     size = len(arr)

# for i in range(cnt):
#     arr.append(0)