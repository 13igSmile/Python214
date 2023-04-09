# Задача 1

# from math import pi
#
# print('Площадь окружности: ', (lambda r: pi * r ** 2)(2))
# print('Площадь прямоугольника: ', (lambda x, y: x * y)(10, 13))
# print('Площадь трапеции: ', (lambda a, b, h: 0.5 * (a + b) * h)(7, 5, 3))


# Задача 2

# def func():
#     return lambda a, b, c: a * b * c
#
#
# d = func()
# print(d(2, 5, 5))

# Задача 3

# a = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# print(sorted(a, key=lambda i: i['name']))
# print(sorted(a, key=lambda i: i['final'], reverse=True))

# Задача 4

# a = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# print(max(a, key=lambda i: i['final']))
# print(min(a, key=lambda i: i['final']))

# Задача 5

# a = [3, 6, 8, 9, 1, 2]
# print(list(map(lambda i: i * a.index(i) ** 3, a)))

# Задача 6

nums = [3, 5, 7, 3, 9, 5, 7, 2]
nums2 = list(map(lambda a: a ** 2, nums))
nums3 = list(map(lambda a: a ** 3, nums))
print(nums2)
print(nums3)
