# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите число: "))

# попробовать разложить на лист левую и правую часть, а потом просуммировать

def SumOfDigitsInNumber(n):
    res = 0
    if n.is_integer():
        while (n != 0):
            res = int(n % 10 + res)
            print(res)
            n = int(n / 10)
            print(n)
    else:
        res = int(n)
        while (n < 1000):
            n = n * 10
            print(n)
            res = int(n % 10) + res
            print(res)
    return res


result = SumOfDigitsInNumber(number)
print(result)
