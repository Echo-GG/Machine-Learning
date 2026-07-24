# 给定两个字符串str1和str2，输出两个字符串的最长公共子串，保证str1和str2的最长公共子串存在且唯一。

def lcs(str1,str2):
    res = ""
    left = 0
    for i in range(len(str1)):
        if str1[left:i+1] in str2:
            res = str1[left:i+1]
        else:
            left += 1
    return res
print(lcs("hellopython","goodlopylike"))