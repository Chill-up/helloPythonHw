# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarterNum = int(input("Введите номер четверти (от 1 до 4): "))

# Сначала сделал так, но потом на switch case переделал

# if quarterNum == 1:
#     print(f"В {quarterNum} четверти возможен диапазон координат от x до y")
# elif quarterNum == 2:
#     print(f"В {quarterNum} четверти возможен диапазон координат от -x до y")
# elif quarterNum == 3:
#     print(f"В {quarterNum} четверти возможен диапазон координат от -x до -y")
# elif quarterNum == 4:
#     print(f"В {quarterNum} четверти возможен диапазон координат от x до -y")
# else:
#     print("Вы ввели не верные данные! ")
match quarterNum: 
    case 1:
        print(f"В четверти {quarterNum} возможен диапазон координат от x до y")
    case 2:
        print(f"В четверти {quarterNum} возможен диапазон координат от -x до y")
    case 3:
        print(f"В четверти {quarterNum} возможендиапазон координат от -x до -y")
    case 4:
        print(f"В четверти {quarterNum} возможен диапазон координат от x до -y")
    case _:
        print("Вы ввели не верные данные! ")