# Задача 1

import random as r

# a = [r.randint(0, 100) for i in range(10)]
# b = max(a)
# print(a)
# print("max:", b)
# a.remove(b)
# a.insert(0, b)
# print(a)

# Задача 2

# a = [r.randint(-20, 20) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)

# Задача 3

a = [r.randint(0, 100)for i in range(10)]
b = min(a)
c = a.index(b)
print(a)
print("min:", b)
print("index min:", c)
del a[0:c]
print(a)
