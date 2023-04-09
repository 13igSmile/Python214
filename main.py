# name = 'Maks'
# print('Hello', name)
# age = 20
# print(age)
# print(id(age))
# age = 'hello'
# print(age)

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, 'Hello', 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# print(type(True))

# a = 1
# b = 2
# print('a =', a)
# print('b =', b)
# c = a
# a = b
# b = c
# print('a =', a)
# print('b =', b)
# a, b = b, a
# print('a =', a)
# print('b =', b)

# print('строка символов')
#
# number = 7 + 3 + 5
# print(number)
#
# number2 = 7 * 5 * 3
# print(number2)
#
# number3 = (5 + 7 + 3) / 3
# print(number3)

# num = 10
# num += 5
# print(num) #15

# num = 4321
# a = num % 10
# # print(a)
# num = num // 10
# # print(num)
# b = num % 10
# # print(b)
# num = num // 10
# # print(num)
# c = num % 10
# # print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
#
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# Функции явного преобразования типов
# str()
# int()
# float()
# bool()

# num1 = '2.5'
# num2 = 3
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.8))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end=" ")
# print("Я учу Python.")

# name = input("Ваше имя: ")
# print(name)

# num = int(input("Введите число: "))
# num1 = int(input("Введите степень: "))
# st = num ** num1
# print("Число", num, "в степени", num1, "равно", st)

# b1 = True
# b2 = False

# print(bool("Python"))
# print(bool(""))  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещён")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# side1 = int(input("Введите первую сторону "))
# side2 = int(input("Введите вторую сторону "))
# side3 = int(input("Введите третью сторону "))
# if side1 == side2 == side3:
#     print("Треугольник равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
# elif day == 6 or day == 7:
#     print("Выходной день")
# else:
#     print("Такого дня недели не существует")

# mon = int(input("Введите номер месяца: "))
# if mon == 12 or mon == 1 or mon == 2:
#     print("Время года зима")
# elif mon == 3 or mon == 4 or mon == 5:
#     print("Время года весна")
# elif mon == 6 or mon == 7 or mon == 8:
#     print("Время года Лето")
# elif mon == 9 or mon == 10 or mon == 11:
#     print("Время года Осень")
# else:
#     print("Ошибка ввода данных")

# crow = int(input("Введите количество ворон от 0 до 9: "))
# if crow == 0 or 5 <= crow <= 9:
#     print("На ветке", crow, "ворон")
# elif crow == 1:
#     print("На ветке", crow, "ворона")
# elif 2 <= crow <= 4:
#     print("На ветке", crow, "вороны")
# else:
#     print("Ошибка ввода")

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')


# day = '1'
# time = 8
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if time >= 9:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print('Дня недели не существует или не рабочее время')

# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 20, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input("Введите делимое: "))
# b = int(input("Введите делитель: "))
# print(a // b if b != 0 else "На ноль делить нельзя")


# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try: # попытаться выполнить
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError): # исключение
#     print("Нельзя вводить строки и делить на ноль")
# else: # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally: # выполняется в любом случае
#     print("Конец программы")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)

# Циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# a = int(input("Укажите количество символов: "))
# b = 0
# while a > b:
#     print("*", end=" ")
#     b += 1

# a = int(input("введите число: "))
# print("*" * a)

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# sum1 = 0
# while a <= b:
#     sum1 += a
#     a += 2
# print('Сумма: ', sum1)

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# sum1 = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2 != 0:
#         sum1 += a
#     a += 1
# print("Сумма нечетных: ", sum1)
#
# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# pr = 1
# while True:
#     a = int(input("Введите число: "))
#     if a == 0:
#         break
#     pr *= a
# print("Результат: ", pr)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j += 1
#     i += 1

# a = 1
# while a < 10:
#     b = 1
#     while b < 10:
#         print(a, '*', b, '=', a * b, '\t\t', end='')
#         b += 1
#     print()
#     a += 1

# for element in collection:
#    тело цикла

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)

# print(range(5))

#  range(start, stop, step)

# for i in range(0, -8, -1):
#     print(i, end=" ")
# print()
# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('\ndone')

# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# print([i for i in "Hello"])

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)

# nums = [8, 3, 9, 4, 1, "Hello", 2.3]
# print(nums)
# print(type(nums[1]))
# print(id(nums))
# print(nums[0])
# print(nums[-1])
#
#
# nums[-2] = 2
# nums[1] += 100
# print(nums)
# print(id(nums[1]))
# print(len(nums))

# s = []
# print(s)
# b = list()
# print(b)
#
# c = list("Hello")
# print(c)

# s = [5, 2] * 6
# print(s)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# n = list(range(2, 10, 2))
# print(n)

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

#  n = 5
# a = [i * 3 for i in "Hello"]
# print(a)

# a = [0] * int(input("Количество элементов в списке: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("Количество элементов в списке: ")))]
# print(a)

# nums = [8, 3, 9, 4, 1]
# print(nums * 2)
# for i in range(len(nums)):  # 0 1 2 3 4
#     print(nums[i] * 2, end=" ")
# print()
# for elem in nums:  # 8 3 9 4 1
#     print(elem * 2, end=" ")

# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
# summ = 0
# for i in a:
#     if i < 0:
#         summ += i
# print(summ)

# a = [i for i in range(21, 41)]
# summ = 0
# odd = 0
# for i in a:
#     if i % 2 != 0:
#         summ += i
#     else:
#         odd += 1
# print("Сумма нечетных элементов: ", summ, "\nКол-во четных: ", odd)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
# summ = 0
# sr = 0
# for i in a:
#     if i != 0:
#         summ += i
#         sr += 1
# print("Среднее: ", summ / sr)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# список[start:stop:step]

# a = [9, 4, 3, 1, 5, 17]
# print(a[1:4:2])
# print(a[:])

# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[3::4])
# print(a[4:])
# print(a[-3:1:-1])
# print(a[2:5])

# a = list(range(1, 8))
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:3] = [20]
# print(a)
# a[2] = 50
# print(a)
# a[3:5] = []
# print(a)
# del a[:]
# print(a)

# Методы списков
# a = list(range(1, 8))
# print(a)
# a.append(99)    # добавляет 1 элемент в конец списка
# print(a)
# a.extend([22, 11, 9])   # добавляет множество элементов в конец списка
# print(a)
# a.insert(0, 100)   # добавляет элемент в список по индексу
# print(a)
# a.extend('add')
# print(a)

# s = []
# n = int(input("Введите количество элементов в списке: "))
# for num in range(n):
#     x = input("-> ")
#     s.append(x)
# print(s)

# a = []
# b = int(input("Введите количество элементов списка: "))
# for i in range(b):
#     c = int(input("Введите число кратное 3: "))
#     if c % 3 == 0:
#         a.append(c)
#     else:
#         print(c, "не делится на 3 без остатся")
# print(a)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# b = [11, 12, 13, 2, 13, 4]
# b.remove(13)    # Удаляет элемент из списка по значению, если элементов несколько, то удаляется только первый
# print(b)
# a = 0
# if a in b:
#     b.remove(a)
# print(b)
#
# last = b.pop(1)  # с пустыми скобками - удаляет последний элемент из списка, с заданным индексом в скобках - удаление
# # по индексу
# print(b)
# print(last)
#
# b.clear()   # Очищает список
# print(b)

# a = [int(input("-> ")) for i in ' ' * int(input("Введите кол-во элементов: "))]
# b = int(input("Введите индекс: "))
# a.pop(b)
# print(a)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# num = a.count(2)    # кол-во заданных значений в списке
# print(num)
# ind = a.index(2, 4)     # возвращает первый индекс искомого значения. Можно указать значения start и end
# print(ind)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# b = a.copy()
# print("a:", a)
# print("b:", b)
# a.append(20)
# print("a:", a)
# print("b:", b)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
# a.reverse()     # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort()    # сортирует список по умолчанию - по возрастанию, reverse=True - по убыванию
# print(a)
#
# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# c = sorted(a)
# print(c)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))     # от 2 по 9 (включительно)
# print(random.randrange(2, 9, 2))

# from random import randint, randrange
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# from random import *
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# import random as r
#
# print(r.randint(2, 9))
# print(r.randrange(2, 9, 2))
# print(round(r.uniform(10.5, 25.5), 3))
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# # city = [1, 5, 4, 6, 7, 8, 9, 2, 3, 0]
# # print(r.choice(city))
# # print(r.choices(city, k=3))
# r.shuffle(city)
# print(city)

# import random as r

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
# print(res)

# x = list('1a2b3c4c')
# print(x)
# print('a' in x)
# print('w' in x)
# print('a' not in x)

# lst = []
# # if len(lst) == 0:
# # if not lst:
# #     print("Список пустой")
# print(bool(lst))

# from random import randint, randrange

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print("Минимальные и максимальные значения обоих списков: ", c)

# a = int(input("Введите размер списка: "))
# b = []
# while len(b) < a:
#     # i = randint(0, a - 1)
#     i = randrange(a)
#     if i not in b:
#         b.append(i)
# print(b)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print([[x for x in row] for row in matrix])

# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
#
# from random import randint

# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# i = 1
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x > 0:
#             i *= x
#     print()
# print("Произведение не нулевых элементов: ", i)

# w = h = 6
# i = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# s = []
# # m = 101
# for i in range(w):
#     s.append(matrix[i][i])
#     if m > matrix[i][i]:
#         m = matrix[i][i]
# print(s)
# print(min(s))

# import math as m
# from math import sqrt, ceil, floor, pi

# num1 = sqrt(4)
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
#
# print(num1)
# print(num2)
# print(num3)
#
# print(pi)

# r = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * r, 2))
# print("Длина окружности: ", round(2 * pi * int(input("Введите радиус окружности: ")), 2))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(4654414541)))
# print(time.strftime("Сегодня: %B %d, %Y"))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "sec.")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res, "sec.")

#   Функции

# def hello(name, word):
#     print("Hello", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol(count, a, b):
#     # print((a + b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# w = get_sum(x, y)
# print(w * 2)

# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(5, 3):
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Этот пароль надежный")
# else:
#     print("Это ненадежный пароль")

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.insert(0, end)
#     lst.append(start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 2))
# print(get_sum(1, 2, d=5))

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name: ", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")

#   Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))

# s = True
# print(id(s))
# s = False
# print(s)
# print(id(s))

#   Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
# b = tuple(a)
# print(type(b))
# print(b)

# t = tuple("Hello")
# print(type(t))
# print(t)
#
# print(t[1])
# print(t[1:3])

# s = tuple(input('-> ') for i in range(3))
# print(s)

# s = input("-> ")
# print(tuple(s))
# from random import randint

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("World")
# t3 = t1 + t2


# print(t3)
# print(len(t3))
#
# print(t3.count('l'))
# print(t3.count('a'))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     while el in tpl:
#         first = tpl.index(el)
#         if tpl.count(el) == 1:
#             return tpl[first:]
#         if tpl.count(el) >= 2:
#             last = tpl.index(el, first + 1)
#             return tpl[first:last + 1]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint


# def tup(tpl1, tpl2):
#     print(tpl1)
#     print(tpl2)
#     print(tpl1 + tpl2, "\n", "0 =", (tpl1 + tpl2).count(0))
#
#
# tup(tuple(randint(0, 5) for i in range(10)), tuple(randint(-5, 0) for j in range(10)))

# def tup(a, b):
#     return tuple(randint(a, b) for _ in range(10))
#
#
# tpl1 = tup(0, 5)
# tpl2 = tup(-5, 0)
#
# print(tpl1)
# print(tpl2)
# print(tpl1 + tpl2, "\n", "0 =", (tpl1 + tpl2).count(0))

# point = (10, 20)
#
# match point:
#     case (0, 0):
#         print("Точка находится в координатах 0:0")
#     case (x, 0):
#         print("Точка находится в координате", x, "по оси X и в координате 0 по оси Y")
#     case (0, y):
#         print("!!!Точка находится в координате 0 по оси X и в координате", y, "по оси Y")
#     case (x, y):
#         print("Точка находится в координате", x, "по оси X и в координате", y, "по оси Y")
#     case _:
#         print("Это не координаты точки")

# t = (10, 11, [1, 2, 3, ], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# a = list(range(2))
# print(a)
# print(a.__sizeof__())
# b = list(range(10))
# print(b)
# print(b.__sizeof__())

#   Распаковка кортежей

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# name1, age1, married1 = get_user()
# # name1, age1, married1 = user
# # user = get_user()
# # name1, age1, married1 = user
# print(name1, age1, married1)

# a = (1, 2)
# del a
# print(a)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# print()
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)

# set() - множество

# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)
# print(type(s))
# print(len(s))

# c = ['red', 'green', 'green', 'blue']
# a = set(c)
# print(type(a))
# print(a)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(a):
#     return set(a), len(set(a))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
# # print(b)
# # print(c)

# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
# print('apple' not in s)
# print(s)
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r}
# c = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# s = {'banana', 'apple', 'orange'}
# s.add(4)  # Добавляет элемент во множество
# if 44 in s:
#     s.remove(44)  # Удаляет элемент по значению
# s.discard(4)  # Удаляет элемент по значению без генерации исключения
# s.pop()  # удаление первого элемента
# s.clear()  # полная очистка множества
# print(s)

#  Операции над множествами
# a = {0, 1, 2, 3, }
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# c = a & b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print('Unic elems count: ', len(s))
# print('max elem: ', max(s))
# print('min elem: ', min(s))

# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
# c = a & b
# print("Общими буквами являются: ", c)
# for i in c:
#     print(i, end=" ")

# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
# c = a - b
# for i in c:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# both_hobby = drawing & music
# print(one_hobby)
# print(both_hobby)
# print(drawing - music)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# s1 = frozenset({'hello', 'world'})
# print(s1)

# Словарь (dict)

# a = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(a[0])
# print(d['one'])

#  d = {'one': 1, 'two': 2}
# d = dict(one=1, two=2)
# print(d)
# print(type(d))

# a = [
#     ('igor@mail.com', 'Igor'),
#     ('irina@mail.com', 'Irina'),
#     ('anna@mail.com', 'Anna'),
# ]
#
# b = dict(a)
# print(b)

# d = {i: 100 for i in range(2,7)}
# print(d)
# print(d[3])
# d[3] = 15
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
# d[(1, 2.3)] = "Новое значение"
# print(d)
# print("two" in d)
# key = 'one1'
# # if key in d:
# #     del d[key]
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + "нет в словаре")
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
#
# for key in d:
#     print(key, " = ", d[key])

# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# b = 1
# for key in a:
#     b *= a[key]
# print(b)

# d = dict()
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], 'руб', sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input("Кол-во: "))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], 'руб', sep="")

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('c', 0)  # получить значение по заданному ключу
# print(value)
# n = d.keys()    # список ключей
# print(n)
# n = d.values()  # список значений
# print(n)
# n = d.items()   # список ключ + значение
# print(n)
#
# for i, j in d.items():
#     print(i, '->', j)

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d.copy()   # создание копии словаря
#
# print("D =", d)
# print("D2 =", d2)
#
# d['b'] = 5
# d2['e'] = 7
#
# print("D =", d)
# print("D2 =", d2)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b')   # удаляет элемент из словаря по ключу, возвращает значение ключа
# print(item)
# print(d)
# item = d.popitem()  # удаляет произвольную пару ключ + значение и возвращает их
# print(item)
# print(d)
# item = d.setdefault('f', 5)     # добавляет ключ со значение по умолчанию, если ключа не существует
# print(item)
# print(d)

# d.update({'a': 20, 'w': 10})    # обновление словаря
# print(d)
# d.update([('q', 7), ('t', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# w = x дут y
# print(w)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# w = x.copy()
# w.update(y)
# print(w)

# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

# new_a = dict()
# new_a['name'] = a.pop('name')
# new_a['salary'] = a.pop('salary')
# new_a = {'name': a.pop('name'), 'salary': a.pop('salary')}
# print(a)
# print(new_a)

# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # a.update({'location': a.pop('city')})
# a['location'] = a.pop('city')
# print(a)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# a = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y, ': ', a[x][y], sep="")
#
# b = input("Имя: ")
# c = input("Регион: ")
# print(a[b][c])
# d = int(input("Новое значение: "))
# # a[b].update({c: d})
# a[b][c] = d
# print(a[b])

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print({k: v for k, v in d.items()})

# value = int(input("-> "))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# value = list(d.keys())
# print(value)
# value = list(d.values())
# print(value)
# value = list(d.items())
# print(value)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []   # d['one'] = []
#         s = i   # s = 'one'
#     else:
#         d[s].append(i)  # d['one']
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = dict(zip(a, b))
# print(d)

# one = {'name': 'Igor', 'last_name': 'Doe', 'Job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'Job': 'Manager'}
#
#  for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
#
# obj = {
#     'one': {'name': 'Igor', 'last_name': 'Doe', 'Job': 'Consultant'},
#     'two': {'name': 'Irina', 'last_name': 'Smith', 'Job': 'Manager'}
# }
# print(obj)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#
# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# data = ['a', 'b', 'c', 'd']

# for i in data:
#     print(i, end=' ')
# print()
# for i in range(len(data)):
#     print(i, end=' ')
# print()
#
# j = 1
#
# for i in data:
#     print(j, ":", i)
#     j += 1

# for j, i in enumerate(data, 1):
#     print(j, ':', i)

# n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for j, (i, v) in enumerate(n.items(), 100):
#     print(j, ':', i, "->", v)

# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)

# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6, 9, 5))
# print(func())


# def to_dict(*args):
#     print(*args)
#     print(args)
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4, ))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def fun(*args):
#     sa = 0
#     new_args = []
#     for i in args:
#         sa += i / len(args)
#     print(sa)
#     for i in args:
#         if i < sa:
#             new_args.append(i)
#     print(new_args, end=' ')
#     print()
#
#
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9)
# fun(3, 6, 1, 9, 5)

# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 3, 4, 'abc'))

# def print_scores(student, *scores):
#     print('Student Name: ', student, end=', scores: ')
#     a, b = None, ""
#     for score in scores:
#         a = str(score) + ", "
#         b += a
#     print(b[:-2])
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33, 56)

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or only_add and i % 2:
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))


# def func(**data):
#     for key, value in data.items():
#         print(key, 'is', value)
#     print()
#
#
# func(name='Irina', surname="Sharma", age=22, phone=1234567890)
# func(name='Igor', surname="Wood", email="igor@mail.ru", country="Russia", age=25, phone=987654320)


# def db(**kwargs):
#     my_dict.update(kwargs)
#     print("my_dict =", my_dict)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')

# def func(a, *args, b=2, **kwargs):
#     print(a, args, kwargs, b)
#
#
# func(4, 5, 6, 7, k1=22, k2=31, k3=11, k4=91)

# Области видимости (scope)

# name = "Tom"  # Глобальная переменная
#
#
# def hi():
#     global name
#     name = 'Sam'    # локальные переменные
#     surname = 'Johnson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()

# def add_two(a):
#     x = 2
#
#     def add_some():
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# max = [8, 1, 2, 4, 5, 6, 9]
# print(min(max))
#
# a = [7, 8, 9, 5]
# print(max(a))

# def outer_func(who):
#     def inner_func():
#         print('Hello,', who)
#
#     inner_func()
#
#
# outer_func('World')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print('a =', a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add = outer(5)
# print(add(10))
# print(add(20))
#
# add1 = outer(6)
# print(add1(10))
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }


# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print('A =', A(students))
# print('B =', B(students))
# print('C =', C(students))
# print('D=', D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())

# lambda (Анонимные функции)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())

# func = lambda *args: args
#
# print(func(1, 2, 3, 4, 5, 6, 7))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))
#
#
# def inc2(n):
#     def func(x):
#         return n + x
#
#     return func
#
#
# a = inc2(42)
# print(a(3))
#
# inc1 = (lambda n: lambda x: n + x)
#
# f1 = inc1(42)
# print(f1(3))
#
# print("!!!", (lambda n: lambda x: n + x)(42)(3))

# print((lambda a, b, c: a + b + c)(2, 4, 6))
# print((lambda d: lambda e: lambda f: d + e + f)(2)(4)(6))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# d = {'b': 15, 'a': 3, 'c': 7}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[3](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
# d[3]()

# print((lambda a, b: a if a > b else b)(12, 5))

# print((lambda a, b, c: a if a < b and a < c else b if b < c and b < a else c)(9, 18, 15))

# map(func, iterable), filter(func, iterable)

# def mul(t):
#     return t * 2


# lst = [2, 8, 12, -5, 10]
#
# # lst2 = list(map(mul, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 100.03)
#
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
#
# print(t2)

# area = [3.45678, 5.676768, 4.001232, 7.45665, 1.4354566, 9.234232]
#
# res = list(map(round, area, [2, 2, 2, 2, 2, 2]))
# print(res)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# sum1 = list(map(lambda x, y: x + y, l1, l2))
# print(sum1)

# filter

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# a = [randint(1, 40) for i in range(10)]
# print(a)
# b = list(filter(lambda i: 10 <= i <= 20, a))
# print(b)

# a = [45, 55, 60, 37, 100, 105, 220]
# b = list(filter(lambda i: i % 15 == 0, a))
# print(b)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)

# Декораторы

# def hello():
#     return 'Hello, i am func "hello"'
#
#
# def super_func(func):
#     print('Hello, i am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, i am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, i am func "func_test')
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func): # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#
#     return func_wrapper
#
#
# @my_decorator   # декоратор
# def func_test():    # декорируемая функция
#     print('Hello, i am func "func_test')
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Назарова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#
#
# print_full_name("Ирина", "Назарова")
# print()
# print_full_name_1("Виктор", "Федорович", "Назаров")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def decor(x):
#     def func(fn):
#         def wrap(y):
#             print("Результат:", x * fn(y))
#
#         return wrap
#
#     return func
#
#
# @decor(3)
# def return_num(num):
#     return num
#
#
# return_num(5)

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных", f_args[i])
#                     # return "Некорректный тип данных"
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных", f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))

# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world("world!")
# hello_world2("Hi!")

print('hello')
