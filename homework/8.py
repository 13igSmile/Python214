from random import randint


# Задача 1

def fun(a):
    print(a)
    for i in a:
        if i > 0 and i % 13 == 0:
            c.append(i)
            # print('->', c)
    return c
#
#
# c = []
# fun(tuple(randint(-13, 39) for i in range(int(input("Введите кол-во чисел: ")))))
# if len(c) == 0:
#     print('Нет положительного числа кратного 13')
# else:
#     print(max(c))

# Задача 2

# a = ('ab', 'abcd', 'cde', 'abc', 'def')
# el = str(input("s = "))
# if el in a:
#     print('Yes')
# else:
#     print('No')

# задача 3

# a = tuple(input("Введите символы кортежа, без пробелов: "))
# print(a)
# for i in a:
#     num = a.count(i)
#     print(i, ' = ', num)
