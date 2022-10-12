# Реализуйте алгоритм перемешивания списка.
import random

number = int(input(
    "Введите число, задающее длину списка и одновременно диапазон значений в этом списке: "))

lst = []
for i in range(number):
    lst.append(random.randint(-number, number))
print(f"Исходный список:\n{lst}")

mixedLst = []
while len(lst) > 0:
    selectIndex = random.choice(range(len(lst)))
    mixedLst.append(lst[selectIndex])
    lst.pop(selectIndex)
print(f"Перемешанный список:\n{mixedLst}")
