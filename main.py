arr = [2, 4, 10, 4, 1]
max_number= max(arr)
max_index = arr.index(max_number)
if max_index == 1:
    sum_left = arr[0] + arr[len(arr)-1]
    sum_rigth = arr[max_index + 1] + arr[max_index +2]
    if sum_left > sum_rigth:
        summa = max_number + sum_left
    else:
        summa = max_number + sum_rigth
    print('сумма =', summa)
elif max_index == len(arr)-1:
    sum_left =  arr[max_index - 1] + arr[max_index -2]
    sum_rigth = arr[0] + arr[1]
    if sum_left > sum_rigth:
        summa = max_number + sum_left
    else:
        summa = max_number + sum_rigth
    print('сумма =', summa)
elif max_index == len(arr)-2:
    sum_left = arr[max_index - 1] + arr[max_index -2]
    sum_rigth = arr[0] + arr[max_index + 1]
    if sum_left > sum_rigth:
        summa = max_number + sum_left
    else:
        summa = max_number + sum_rigth
    print('сумма =', summa)
elif max_index == 0:
    sum_left = arr[len(arr)-2] + arr[len(arr)-1]
    sum_rigth = arr[max_index + 1] + arr[max_index +2]
    if sum_left > sum_rigth:
        summa = max_number + sum_left
    else:
        summa = max_number + sum_rigth
    print('сумма =', summa)
elif max_index > 1 and max_index < len(arr)- 2:
    sum_left = arr[max_index - 1] + arr[max_index -2]
    sum_rigth = arr[max_index + 1] + arr[max_index + 2]
    if sum_left > sum_rigth:
        summa = max_number + sum_left
    elif sum_left == sum_rigth:
        a = arr[max_index - 1]
        b = arr[max_index - 2]
        c = arr[max_index + 1]
        d = arr[max_index + 2]
        if a > b and c> d:
            summa = max_number + a + c
        elif a < b and c < d:
            summa = max_number + b + d
        elif a > b and c < d:
            summa = max_number + a + d
    print('сумма =', summa)
# print(max_number)
# print(max_index)
