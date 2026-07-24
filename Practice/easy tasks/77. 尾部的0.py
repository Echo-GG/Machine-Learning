# 给定一个整数n，计算出n!中尾部的0的个数。
def factorial(n):
    if n == 1 :
        return 1
    return n * factorial(n-1)
n = int(input("请输入一个整数n: "))
N = factorial(n)
count = 0
temp = N
while temp!=0:
    if temp % 10 != 0:
        break
    else:
        count += 1
        temp/=10
print(count)