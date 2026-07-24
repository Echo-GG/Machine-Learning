# 给定一个非负整数n，请问是否存在一个x满足2^x = n，如果有，则返回true，否则返回false。

def func(n):
    i = 0
    while(pow(2,i)<n):
        i += 1
        if pow(2,i) == n:
            return True
    return False
n = int(input("请输入一个非负整数n: "))
print(func(n))

# Another solution:

# 0100(4) 1000(8)
# 0011(3) 0111(7)

def func(n):
    return n > 0 and n & (n - 1) == 0

print(func(n))