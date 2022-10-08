# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число N: "))

def MultiplyDigitsFrom1toN(n):
    res = []
    for i in range(1, n+1):
        res.append(i)
    for j in range(1, n):
        res[j] = res[j-1] * (j+1)
    return (res)

result = MultiplyDigitsFrom1toN(number)
print(f'Набор произведений чисел от 1 до {number} = {result}')
