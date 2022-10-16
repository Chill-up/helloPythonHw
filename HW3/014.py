# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи] в Wiki надо читать

number = int(
    input("Введите число желаемых чисел Фибоначчи: "))

fiboList = [0, 1]


def Fibo(n):
    lst = [0, 1]
    negaLst = [1, -1] #после переверота будет правильный порядок
    if number in lst:
        return fiboList
    else:
        for i in range(2, n+1):
            lst.append(lst[i-1]+lst[i-2])
        for j in range(3, n+1):
            negaLst.append(lst[j] * pow(-1, j+1))
        negaLst.reverse()
        return (negaLst + lst)


res = Fibo(number)
print(
    f"Cписок {number} чисел Фибоначчи, в том числе для отрицательных индексов:\n{res}")
