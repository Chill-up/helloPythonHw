# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def FindPrimeMultipliers(n):
    multipliersList = []
    divider = 2
    while n > 1:
        if n % divider == 0:
            multipliersList.append(divider)
            n = n / divider
        else:
            divider += 1
    return multipliersList


while (True):
    numberN = int(input("Введите натуральное число > 1: "))
    if numberN <= 1:
        print("Невозможно найти множители для этого числа.\n")
    else:
        res = FindPrimeMultipliers(numberN)
        print(res)
        break
