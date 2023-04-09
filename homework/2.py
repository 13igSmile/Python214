n = int(input("Введите число от 1 до 99: "))
kop = n
if 11 <= kop <= 14:
    print(n, "копеек")
elif 0 <= n <= 10 or 15 <= n <= 99:
    kop = kop % 10
    if kop == 1:
        print(n, "копейка")
    elif 2 <= kop <= 4:
        print(n, "копейки")
    else:
        print(n, "копеек")
else:
    print("Ошибка ввода")
