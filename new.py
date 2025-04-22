a = [1, 1, 2, 3, 1, 1, 1, 1, 2, 3]
min_1 = a[0]
min_2 = a[1]
for x in a:
    if x < min_1:
        min_2 = min_1
        min_1 = x
    elif min_1 < x < min_2:
        min_2 = x
    elif min_2 == min_1 != x:
            min_2 = x
if min_2 == min_1:
    print('В заданном массиве все элементы одинаковые')
else:  
    print(min_1, min_2)