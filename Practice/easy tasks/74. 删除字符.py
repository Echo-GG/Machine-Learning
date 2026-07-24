# 给定两个字符串str和sub，从str中完全删除在sub中存在的字符。
str = "Thank youu!"
sub = "you"

def dele(str,sub):
    s = set(sub)
    ans = ''
    for i in str:
        if i not in s:
            ans += i
    return ans

print(dele(str,sub))