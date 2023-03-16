# Задача 14: Требуется вывести все целые степени двойки (т.е. числа # вида 2k, не превосходящие числа N.
# 10 -> 1 2 4 8


number = int(input('Введите число '))
numsquare = 1
degree = -1
while numsquare <= number:
    numsquare *= 2
    degree += 1
    print(degree, end=' ')
