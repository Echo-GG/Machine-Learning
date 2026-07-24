# 给定两个字符串，判断其中一个字符串是否为另一个字符串的置换。
# 置换：通过改变顺序可以使两个字符串相等
def func(s1,s2):
    if len(s1) != len(s2):
        return False
    lst1 = [s for s in s1]
    lst2 = [s for s in s2]
    return lst1.sort() == lst2.sort()
s1 = input()
s2 = input()
print(func(s1,s2))

# Another solution:
def func(A,B):
    A = sorted(A)
    B = sorted(B)
    return A == B
print(func(s1,s2))