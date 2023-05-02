a = [5, 9, 6, 7]
b = [3, 11, 8]
c = [2, 4]
d = [10, 1, 12]
sort = int(input('Введите 1 или 2 для сортировки по убыванию или возрастанию: '))


def quick_sort(s):
    if sort == 1:
        if len(s) > 1:
            x = s[(len(s) - 1) // 2]

            low = [i for i in s if i < x]
            eq = [i for i in s if i == x]
            hi = [i for i in s if i > x]
            s = quick_sort(hi) + eq + quick_sort(low)

        return s

    if sort == 2:
        if len(s) > 1:
            x = s[(len(s) - 1) // 2]

            low = [i for i in s if i < x]
            eq = [i for i in s if i == x]
            hi = [i for i in s if i > x]
            s = quick_sort(low) + eq + quick_sort(hi)

        return s


lst = a + b + c + d
lst = quick_sort(lst)


def search(s, item):
    for i in range(len(s)):
        if s[i] == item:
            return item
    return -1


print(lst)
res = search(lst, int(input('Введите значение для поиска: ')))
if res == -1:
    print('Значение не найдено')
else:
    print('Значение', res, 'найдено')
