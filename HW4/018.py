# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
#
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from encodings import utf_8
from random import randint as rI

numberK = int(input("Задайте желаемую натуральную степень: "))

koefList = {}
for i in range(numberK, -1, -1):
    koefList[i] = rI(-100, 100)

result = ""
firstIteration = True
for i in koefList.items():
    if firstIteration:
        firstIteration = False
        if i[1] < 0:
            result += " -" + str(abs(i[1])) + "x^" + str(i[0])
        elif i[1] > 0:
            result += str(abs(i[1])) + "x^" + str(i[0])
    else:
        if i[1] < 0:
            result += " - " + str(abs(i[1])) + "x^" + str(i[0])
        elif i[1] > 0:
            result += " + " + str(abs(i[1])) + "x^" + str(i[0])


with open("018.txt", encoding="utf-8", mode="w") as file:
    file.write(
        f"Для заданного коэффициента k = {numberK} сформирован следующий многочлен:\n")
    file.write(result.replace("x^1", "x").replace("x^0", "") + " = 0")
