# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def ConvertFloatToInt(num):
    multiplier = int(1)
    intNum = float(num)
    while not intNum.is_integer():
        multiplier *= 10
        intNum = num * multiplier
    return int(intNum)

def SumOfDigitsInNumber(n):
    intN = ConvertFloatToInt(n)
    intN = abs(intN)
    sum = 0
    while intN > 0:
        sum += intN % 10
        intN //= 10
    return sum

number = float(input("Введите любое вещественное число: "))
print(f"Сумма цифр введенного числа = {SumOfDigitsInNumber(number)}")
