# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284




def sum_del(p):
    summa = 0
    for e in range(1, p // 2 + 1):
        if p % e == 0:
            summa += e

    return summa

k = 10000
for n in range (1, k):
    m = sum_del(n)
    if n < m <= k and n == sum_del(m):
        print(n, m)



# def deviders(number: int) -> int:
#     list_dev = []
#     for div in range(1, number//2 + 1):
#         if not number % div:
#             list_dev.append(div)
#     return sum(list_dev)


# unique_list = []
# for num in range(10000):
#     if deviders(deviders(num)) == num and num != deviders(num):
#         if not ((num, deviders(num))) in unique_list:
#             unique_list.append((deviders(num), num))
#             print(num, deviders(num))