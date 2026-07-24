bills1 = [5,10,10,20,10,10,5,5,5,20,20,20]
bills2 = [5,5,5,10,20]
def func(bills):
    five = 0
    ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True
print(func(bills1))
print(func(bills2))