# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
#
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random
number = int(input("Задайте желаемую длину последовательности (целое число): "))


def printNumbersFromList(list):
    for i in range(len(list)):
        print(int(list[i]), end="")


initLst = []
clearLst = []


for i in range(number):
    initLst.append(random.randint(1, 9))


for i in range(len((initLst))):
    f = initLst[i]
    if initLst.count(f) == 1:
        clearLst.append(f)


print(f"Сгенерирована следующая последовательность цифр:")
printNumbersFromList(initLst)
print(
    f"\nСписок неповторяющихся элементов исходной последовательности\n{clearLst}")
