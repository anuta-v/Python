# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120 

number = abs(int(input('Введите число ')))
factorial = 1

while number > 1:
    factorial*= number
    number -= 1
print(factorial)


"""Решение через while
print('Введите целое неотрицательное число N: ')
n = int(input())
factotial = 1
while n > 1:
    factotial *= n
    n -= 1
print(f'Факториал N равен {factotial}')
"""

"""# Решение через for

print('Введите целое неотрицательное число N: ')
n = int(input())
factotial = 1
i = 1
for i in range(2, n+1):   # от 2, т.к. factorial=1 (умножение на 1 заложили в переменную)
    factotial *= i        # в отличие от С# увеличение счетчика, прописываем в range
print(f'Факториал N равен {factotial}')   # по умолчанию он i++
"""