# 字符串旋转；
# 给定两字符串A和B，如果能将A从中间某个位置分割为左右两部分字符串（可以为空串），
# 并将左边的字符串移动到右边字符串后面组成新的字符串可以变为字符串B时返回true。

def isRotated1(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        rotated = str1[i+1:] + str1[:i+1]  
        if rotated == str2:
            return True
    return False

# Another solution:
def isRotated2(str1,str2):
    return len(str1) == len(str2) and str2 in str1 + str1

A = "hello"
B = "llohe"
print(isRotated1(A,B))
print(isRotated2(A,B))