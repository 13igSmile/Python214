# Задача 1
# rand = 7
# att = 0
# a = int(input("Отгадайте число от 1 до 100 или введите 0 для завершения: "))
# while a != rand:
#     if a > rand and a != 0:
#         att += 1
#         a = int(input("Загаданное число меньше, попробуйте еще: "))
#     if a < rand and a != 0:
#         att += 1
#         a = int(input("Загаданное число больше, попробуйте еще: "))
#     if a == 0:
#         print("Игра завершена")
#         break
# else:
#     att += 1
#     print("Вы отгадали число с", att, "раза")

# Задача 2

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")

# Задача 3

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in a:
#     if a.count(i) == 1:
#         print(i, end=" ")

# Задача 4

print(*["*" * i for i in range(8, 0, -1)], sep="\n")
