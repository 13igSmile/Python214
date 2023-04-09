# Задача 1

# a = int(input("Введите количество символов: "))
# b = input("Введите тип символа: ")
# c = int(input("Введите ориентацию линии: "))   # 0 - горизонтальная, 1 - вертикальная
# d = 0
# while a > d:
#     if c == 0:
#         print(b, end='')
#         d += 1
#     else:
#         print(b)
#         d += 1

# Задача 2

# a = '+'
# b = 1
# while b < 5:
#     print(a * 15)
#     c = '-'
#     d = 1
#     while d == 1:
#         print(c * 15)
#         d += 1
#     b += 1

# Задача 3

# a, b, c = int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))
# max1 = (a if a > c else c) if a > b else (b if b > c else c)
# print(max1)

# Задача 4

# 1 - 'r',   2 - '+',   3 - '-',   4 - '/',   5 - '*',    6 - '%',   7 - '<',   8 - '>'

a, b, c, d, e, f, g, h = 1, 2, 3, 4, 5, 6, 7, 8
i = int(input('Введите цифру: '))
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

while i < 9:
    if i == 1:
        w = -x
        z = -y
        print(w, z)
        break
    elif i == 2:
        print(x + y)
        break
    elif i == 3:
        print(x - y)
        break
    elif i == 4:
        print(x / y)
        break
    elif i == 5:
        print(x * y)
        break
    elif i == 6:
        print(x % y)
        break
    elif i == 7:
        print(x if x < y else y)
        break
    elif i == 8:
        print(x if x > y else y)
        break






