IP = input("请输入一个IP地址: ")
IPv4 = IP.split('.')
# print(IPv4)
bins = []
for ip in IPv4:
    temp = format((int(ip)),'08b')
    bins.append(temp)
# print(bins)
res = ""
for bin in bins:
    res += bin
# print(res)
res = int(res,2)
print(res)

# Another solution:
def func(str):
    strs = str.split('.')
    res = ''
    for i in strs:
        # 十进制转二进制高位补0
        # '{:08b}'.format(val)
        res += '{:08b}'.format(int(i))
    return int(res,2)
print(func(IP))