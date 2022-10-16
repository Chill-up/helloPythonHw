# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет, их в расчет не берем.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
from unittest import result

lst = []
for i in range(5):
    lst.append(round(random.random()*10,2))

print(f"Сгенерирован следующий список чисел:\n{lst}")

result = 0.0
lstCut = []
for i in range(len(lst)):
    if not lst[i].is_integer():
        lstCut.append(round(lst[i]*100%100))
result = (max(lstCut)-min(lstCut))/100

print(f"Разница между максимальным и минимальным значением дробной части элементов = {result}")