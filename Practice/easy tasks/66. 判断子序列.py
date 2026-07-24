# 给定两个字符串S和T，判断S是否是T的子序列。即是否可以从T删除一些字符转换成S。
def func(S,T):
    if len(S) > len(T):
        return False
    idx = 0
    res = ""
    for i in T:
        if S[idx] == i:
            res += i
            idx += 1
        if res == S:
            return True
    return False
print(func('hlo','hello'))
