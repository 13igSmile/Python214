#   Задача 1

# from math import pi, sqrt
#
# s = int(input("Выберите фигуру: 1 - треугольник, 2 - прямоугольник, 3 - круг: "))
# if s == 1:
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     c = int(input("Введите сторону c: "))
#     p = (a + b + c)/2
#     print("Площадь треугольника: ", round(sqrt(p * (p - a) * (p - b) * (p - c)), 2))
# if s == 2:
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     print("Площадь прямоугольника: ", a * b)
# if s == 3:
#     r = int(input("Введите радиус: "))
#     print("Площадь круга: ", round(pi * r ** 2, 2))

#   Задача 2

from random import randint

w = h = 6
matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]

for row in matrix:
    for x in row:
        print(x, end="\t")
    print()
print()

m = matrix.copy()
m[0], m[1] = m[1], m[0]
m[2], m[3] = m[3], m[2]
m[4], m[5] = m[5], m[4]

for row in m:
    for x in row:
        print(x, end="\t")
    print()


