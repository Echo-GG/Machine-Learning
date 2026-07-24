# 给定一个仅由英文小写字母组成的字符串ss，将相邻且相同的两个字符删掉构成新的字符串，
# 重复删除操作直至生成不符合删除条件的字符串并返回。
# e.g.
# 输入: 'acbbc'
# 输出: 'a'

def func(s):
    res = ''
    for i in s:
        if res == '':
            res += i
        elif res[-1] == i:
            res = res[:-1]
        else:
            res += i
    return res

str = input("请输入一个字符串: ")
print(func(str))