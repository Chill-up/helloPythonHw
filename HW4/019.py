# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
from random import randint as rI


def GenerateKoefs():
    res = {}
    numberKoef = int(
        input("Задайте максимальный коэффициент для первого многочлена: "))
    for i in range(numberKoef, -1, -1):
        res[i] = rI(-100, 100)
    return res


def GenerateEquation(kList):
    result = ""
    firstIteration = True
    for i in kList.items():
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
    return result + " = 0"


def parseEquation(eqt: str):
    eqt = eqt.replace(" + ", " +").replace(" - ", " -")
    eqt = eqt.split()
    eqt = eqt[:-2]
    dictEquation = {}
    for i in range(len(eqt)):
        eqt[i] = eqt[i].replace("+", "").split("x^")
        dictEquation[int(eqt[i][1])] = int(eqt[i][0])
    return dictEquation


with open("0191.txt", encoding="utf-8", mode="w") as file:
    file.write(GenerateEquation(GenerateKoefs()))


with open("0192.txt", encoding="utf-8", mode="w") as file:
    file.write(GenerateEquation(GenerateKoefs()))


with open("0191.txt", encoding="utf-8", mode="r") as file1:
    eq1 = file1.readline()

with open("0192.txt", encoding="utf-8", mode="r") as file2:
    eq2 = file2.readline()

parseEq1 = (parseEquation(eq1))
parseEq2 = (parseEquation(eq2))

resultEquation = {}
for i in range(max(len(parseEq1), len(parseEq2)), -1, -1):
    first = parseEq1.get(i)
    second = parseEq2.get(i)
    if first != None or second != None:
        resultEquation[i] = (first if first != None else 0) + \
            (second if second != None else 0)


def printEquation(equation: str):
    print(equation.replace(" 1x", "x")
          .replace("x^1", 'x')
          .replace("x^0", ''))


printEquation(f"Первый многочлен: \n{eq1}\n")
printEquation(f"Второй многочлен: \n{eq2}\n")
print()
printEquation(f"Сумма двух многочленов: \n {GenerateEquation(resultEquation)}")
