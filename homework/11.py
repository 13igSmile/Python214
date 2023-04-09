# Задача 1

# s = 0
#
#
# def func1(a, b, c):
#     def func2(d, e):
#         global s
#         return d * e
#
#     s = 2 * (func2(a, b) + func2(a, c) + func2(b, c))
#     return s
#
#
# print(func1(2, 4, 6))
# print(func1(5, 8, 2))
# print(func1(1, 6, 8))


# Задача 2

# def func1(a, b, c):
#     def func2(d, e):
#         return d * e
#
#     s = 2 * (func2(a, b) + func2(a, c) + func2(b, c))
#     return s
#
#
# print(func1(2, 4, 6))
# print(func1(5, 8, 2))
# print(func1(1, 6, 8))


# Задача 3

def func1(a, b, c):
    s = 0

    def func2(d, e):
        nonlocal s
        s += d * e

    func2(a, b)
    func2(a, c)
    func2(b, c)
    return 2 * s


print(func1(2, 4, 6))
print(func1(5, 8, 2))
print(func1(1, 6, 8))
