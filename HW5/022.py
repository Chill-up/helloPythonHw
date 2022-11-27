# Создайте программу для игры в 'Крестики-нолики'.

position = []
moves = []
win = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3],
       [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
sign = "O"
end = 0

for i in range(1, 10):
    position.append(i)


def PrintField(position):
    print(f"{position[0]:^5}|{position[1]:^5}|{position[2]:^5}")
    print("----------------------")
    print(f"{position[3]:^5}|{position[4]:^5}|{position[5]:^5}")
    print("----------------------")
    print(f"{position[6]:^5}|{position[7]:^5}|{position[8]:^5}")


def WinCondition():
    for i in win:
            print(position[i[0]-1])
            print(position[i[1]-1])
            print(position[i[2]-1])

            if position[i[0]-1] == position[i[1]-1] == position[i[2]-1]:
                print("Game over")
                PrintField(position)
                return 1
            else:
                return 0



while end == 0:
    while True:
        PrintField(position)
        index = int(
            input(f"\n\nХод {'игрока' if sign == 'X' else 'противника'}: "))
        if index in moves:
            print("Эта клетка уже занята.")
        else:
            if sign == "O":
                sign = "X"
            else:
                sign = "O"
            moves.append(index)
            position[index-1] = sign
            end = WinCondition()
        break
