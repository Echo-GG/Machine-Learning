# 将有序数组A和B合并，要求合并后的新数组也要有序
A = [1,2,3,4,7,9,10]
B = [-1,0,2,3,4,4,8,10,11]
res = []
for i in A:
    res.append(i)
for i in B:
    res.append(i)
res.sort()
print(res)

# Another solution:
def func(A,B):
    i,j = 0,0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
    return C
print(func(A,B))