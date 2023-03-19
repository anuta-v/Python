# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


import  random

my_list = [random.randint (0,10) for i in range(10)]
shift = int(input("На сколько двигаем вправо "))
print(my_list)
for i in range(shift):
    temp = my_list.pop(len(my_list)-1)
    my_list.insert(0, temp)
print(my_list)


# Второй вариант
# import  random
# my_list = [random.randint (0,10) for i in range(10)]
# shift = int(input("На сколько двигаем вправо "))
# print(my_list)
# print(my_list[-shift:] + my_list[:-shift])