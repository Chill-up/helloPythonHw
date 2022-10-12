# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
number = int(input("Введите число N: "))

lst = []
for i in range(number):
    lst.append(random.randint(-number, number))
print(
    f"Сгенерирован следующий список:\n{lst}")
path = "./file.txt"
data = open(path, "w+")
data.write(str(random.randrange(0, number)))
data.write("\n")
data.write(str(random.randrange(0, number)))
data.close

with open(path, "r") as data:
    multipleIndexes = data.read().split("\n")
data.close

result = lst[int(multipleIndexes[0])] * lst[int(multipleIndexes[1])]
print(
    f"Сгенерированы, записаны и прочитаны из файла позиции для перемножения, это {multipleIndexes[0]} и {multipleIndexes[1]}(считаем от нуля).\nНа этих позициях находятся числа {lst[int(multipleIndexes[0])]} и {lst[int(multipleIndexes[1])]}.\nИх произведение = {result}")
