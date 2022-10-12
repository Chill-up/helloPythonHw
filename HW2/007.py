# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

import math

number = int(input("Введите число N: "))


def Sequence(n):
    lst = []
    sum = 0
    for i in range(0, n):
        lst.append(math.pow((1+(1/n)), n))
        sum = sum + lst[i]
    return (sum)


result = round(Sequence(number))
print(
    f"Сумма чисел последовательности (1+1/n)^n из {number} элементов = {result}")
