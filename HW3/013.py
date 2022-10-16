# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Деление с остатком на 2 и собрать в обратном порядке

number = int(
    input("Введите число, которое хотите преобразовать в двоичный формат: "))


def Dec2Bin(n):
    binList = []
    while not int(n/2 == 0):
        binNumber = n % 2
        binList.append(binNumber)
        n = int(n / 2)
    for i in range(int(len(binList)/2)): #меняем порядок элементов
        temp = binList[i]
        binList[i] = binList[(-1-i)]
        binList[(-1-i)] = temp
    return (binList)

def PrintBin(listBin): #костыль для вывода цифр, а не списка.
    for i in range(len(listBin)):
       print(listBin[i], end="")


res = Dec2Bin(number)

print(f"Число {number} в двоичном представлении:") 
PrintBin(res)