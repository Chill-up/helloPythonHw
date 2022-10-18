# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math

numberD = float(
    input("Введите интересующую точность, от 0.1 до 0.0000000001: "))

numDigits = 0

while not numberD == int(numberD):
    numberD *= 10
    numDigits += 1

print(f"Запрошенная точность знаков = {numDigits}")

print(
    f"Число Пи с округлением до {numDigits} знаков = {round(math.pi,numDigits)}")
