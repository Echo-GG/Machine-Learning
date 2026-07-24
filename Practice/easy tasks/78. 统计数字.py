# 给定一个数字k，计算k在0到n中出现的次数。
n = 114514
k = 3
k_str = str(k)
count = 0
for i in range(n + 1):
    for s in str(i):
        if s == k_str:
            count += 1
print(count)

# Another solution:
def func(k,n):
    count = 0
    for i in range(n+1):
        time = str(i).count(str(k))
        count += time
    return count

print(func(k,n))
