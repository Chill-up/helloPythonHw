# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt
from decimal import Decimal

A = []
B = []
A.append(int(input("Введите координату x первой точки (A): ")))
A.append(int(input("Введите координату y первой точки (A): ")))
B.append(int(input("Введите координату x второй точки (B): ")))
B.append(int(input("Введите координату y второй точки (B): ")))

res = round(sqrt(pow((B[0] - A[0]), 2) + pow((B[1] - A[1]), 2)),2)

print(f"Расстояние между точками A {A} и B {B} -> {res}")