# 给定一个数，在数字的任意位置插入一个5，使得插入后的这个数字最大。
def insert_5(num):
    if num > 0:
        num_str = str(num)
        new_str = ""
        i = 0
        while i < len(num_str) and int(num_str[i]) >= 5:
            i += 1
        new_str = num_str[:i] + "5" + num_str[i:]
        return int(new_str)
    elif num == 0:
        return 50
    else:
        num_str = str(-num)
        new_str = ""
        i = 0
        while i < len(num_str) and int(num_str[i]) <= 5 :
            i += 1
        new_str = num_str[:i] + "5" + num_str[i:]
        return -int(new_str)        
num = int(input("请输入一个整数: "))
print(insert_5(num))

# Another solution:
def func(a):
    string = ''
    ans = 0
    n = 0
    flag = False
    if a >=0:
        string = str(a)
        n = len(string)
        for i in range(n):
            if (ord(string[i]) - ord('0') < 5 and flag == False):
                ans = ans * 10 + 5
                flag = True
            ans = ans * 10 + ord(string[i] - ord('0'))
        if flag == False:
            ans = ans * 10 + 5
    else:
        a = -a
        string = str(a)
        n = len(string)
        for i in range(n):
            if (ord(string[i]) - ord('0') > 5 and flag == False):
                ans = ans * 10 + 5
                flag = True
            ans = ans * 10 + ord(string[i]) - ord('0')
        if flag == False:
            ans = ans * 10 + 5
        ans = -ans
    return ans
print(func(num))