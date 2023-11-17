#В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.
# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.
# # arr = [, 4, 10, 4, 1]
# max_number= max(arr)
# max_index = arr.index(max_number)
# if max_index == 1:
#     sum_left = arr[0] + arr[len(arr)-1]
#     sum_rigth = arr[max_index + 1] + arr[max_index +2]
#     if sum_left > sum_rigth:
#         summa = max_number + sum_left
#     else:
#         summa = max_number + sum_rigth
#     print('сумма =', summa)
# elif max_index == len(arr)-1:
#     sum_left =  arr[max_index - 1] + arr[max_index -2]
#     sum_rigth = arr[0] + arr[1]
#     if sum_left > sum_rigth:
#         summa = max_number + sum_left
#     else:
#         summa = max_number + sum_rigth
#     print('сумма =', summa)
# elif max_index == len(arr)-2:
#     sum_left = arr[max_index - 1] + arr[max_index -2]
#     sum_rigth = arr[0] + arr[max_index + 1]
#     if sum_left > sum_rigth:
#         summa = max_number + sum_left
#     else:
#         summa = max_number + sum_rigth
#     print('сумма =', summa)
# elif max_index == 0:
#     sum_left = arr[len(arr)-2] + arr[len(arr)-1]
#     sum_rigth = arr[max_index + 1] + arr[max_index +2]
#     if sum_left > sum_rigth:
#         summa = max_number + sum_left
#     else:
#         summa = max_number + sum_rigth
#     print('сумма =', summa)
# elif max_index > 1 and max_index < len(arr)- 2:
#     sum_left = arr[max_index - 1] + arr[max_index -2]
#     sum_rigth = arr[max_index + 1] + arr[max_index + 2]
#     if sum_left > sum_rigth:
#         summa = max_number + sum_left
#     elif sum_left == sum_rigth:
#         a = arr[max_index - 1]
#         b = arr[max_index - 2]
#         c = arr[max_index + 1]
#         d = arr[max_index + 2]
#         if a > b and c> d:
#             summa = max_number + a + c
#         elif a < b and c < d:
#             summa = max_number + b + d
#         elif a > b and c < d:
#             summa = max_number + a + d
#     print('сумма =', summa)
# print(max_number)
# print(max_index)

# правильное решение задачи ниже
# arr = [5, 8, 6, 4, 10, 2, 7, 3]
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# # Вывод максимальной урожайности, которую может собрать собирающий модуль
# print(max(arr_count))
# print(arr_count)