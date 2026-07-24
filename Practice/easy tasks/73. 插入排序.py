def insert_sort(lst):
    for i in range(1,len(lst)):
        j = i - 1
        key = lst[i]
        while j >= 0:
            if lst[j] > key:
                lst[j+1] = lst[j]
                lst[j] = key
            j -= 1
    return lst
lst = [5,78,23,1,2]
print(insert_sort(lst))