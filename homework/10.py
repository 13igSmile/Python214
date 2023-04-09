#   Задача 1

# a = ['red', 'green', 'blue']
# b = ['#FF0000', '#008000', '#0000FF']
# c = {}
# for i in range(len(a)):
#     c[a[i]] = b[i]
# print(c)

#   задача 2

# a = {i: i ** 3 for i in range(1, 11)}
# print(a)

#   Задача 3

# a = ['color', 'fruit', 'pet']
# b = ['blue', 'apple', 'dog']
# c = dict(zip(a, b))
# print(c)

#   Задача 4

from random import randint


# def func(*args):
#     print(*args)
#     for i in args:
#         min1 = min(i)
#         return min1
#
#
# print(func(list(randint(3, 15) for i in range(10))))
# print(func(list(randint(3, 25) for j in range(5))))
# print(func(list(randint(3, 9) for k in range(7))))

#   Задача 5

def func(*args):
    print(args)
    sum1 = 0
    for i in args:
        sum1 += i
        print(sum1, end=' ')
    print()


func(10, 9, 11)
func(2, 3, 4, 9, 5)
func(3, 5, 10, 6, 7, 24)
