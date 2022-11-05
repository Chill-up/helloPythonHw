# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

candies = 150
player1Candies = 0
player2Candies = 0
botCandies = 0

def coinFlip():
    coin = randint(0,1)
    return coin

def playerTurn(playerCandies, dealerCandies):
    turnCandies = 0
    print(f"Сейчас у вас {playerCandies} конфет. Всего осталось {dealerCandies} конфет")
    print("Cколько вы хотите взять?")
    while turnCandies <= 0 or turnCandies > 28:
        turnCandies = int(input("Введите количество от 1 до 28:\n"))
#   print(turnCandys)
    return turnCandies

def botTurn(botCand, dealerCandies):
    turnCand = 0
    print(f"Сейчас у бота {botCand} конфет. Всего осталось {dealerCandies} конфет")
    print()
    if dealerCandies == 28:
        turnCand = 28
    elif dealerCandies == 30:
        turnCand = 1
    elif dealerCandies < 28:
        turnCand = dealerCandies
    else:
        turnCand = randint(1,28)
    print(f"Бот взял {turnCand} конфет")
    print()
    print(f"Сейчас у бота {botCand + turnCand}")
    return turnCand


turn = coinFlip()
if turn == 0:
    print("Первым ходит игрок")
else:
    print("Первым ходит бот")


while True:
    if turn == 0:
        print("\n__________________________________________________\n" + "\nХод игрока 1" + "\n" + "__________________________________________________\n")
        turnR = 0
        turnR = playerTurn(player1Candies, candies)
        player1Candies = player1Candies + turnR
        candies = candies - turnR
        if candies == 0:
            player1Candies = player1Candies + player2Candies + botCandies
            player2Candies = 0
            botCandies = 0
            print(f"\n$$$$$$$$$$$$$$$$$$$$$$ Вы выиграли! Вам достается {player1Candies} конфет $$$$$$$$$$$$$$$$$$$$$$\n")
            break
        turn = 1
    # else:
    #     print("\n__________________________________________________\n" + "Ход игрока 2" + "\n" + "__________________________________________________\n")
    #     turnRes = 0
    #     turnRes = playerTurn(player2Candies, candies)
    #     player2Candies = player2Candies + turnRes
    #     candies = candies - turnRes
    #     if candies == 0:
    #         player2Candies = player2Candies + player1Candies
    #         player1Candies = 0
    #         print(f"\n$$$$$$$$$$$$$$$$$$$$$$ Вы выиграли! Вам достается {player2Candies} конфет $$$$$$$$$$$$$$$$$$$$$$\n")
    #         break
    #     turn = 0
    else:
        print("\n__________________________________________________\n" + "\nХод бота" + "\n" + "__________________________________________________\n")
        turnR = 0
        turnR = botTurn(botCandies, candies)
        botCandies = botCandies + turnR
        candies = candies - turnR
        if candies == 0:
            botCandies = botCandies + player1Candies
            player1Candies = 0
            print(f"\n$$$$$$$$$$$$$$$$$$$$$$ Бот выиграл! Ему достается {botCandies} конфет $$$$$$$$$$$$$$$$$$$$$$\n")
            break
        turn = 0
