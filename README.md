# Репозиторий для домашних задач по введению в Python

## 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

## 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

## 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

x=34; y=-30 -> 4

x=2; y=4-> 1

x=-34; y=-30 -> 3

## 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

## 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

A (3,6); B (2,1) -> 5,09

A (7,-5); B (1,-1) -> 7,21

## 6. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

## 7. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

## 8. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 

Позиции хранятся в файле file.txt в одной строке одно число.

## 9. Реализуйте алгоритм перемешивания списка.

## 10. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

## 11. Напишите программу, которая найдёт произведение пар чисел списка.

Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]

## 12. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет, их в расчет не берем.

*Пример:*

[1.1, 1.2, 3.1, 5, 10.01] => 0.19

## 13. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

45 -> 101101

3 -> 11

2 -> 10

## 14. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

## 15. Вычислить число c заданной точностью *d*

Пример:

при d = 0.001, π = 3.141

при d = 0.1, π = 3.1

при d = 0.00001, π = 3.14154

d от 0.1 до 0.0000000001

## 16. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.