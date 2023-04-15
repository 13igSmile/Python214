# Задача 1

# a = 'I am learning Python. hello, WORLD!'
# a = a[:a.find('h')] + a[a.rfind('h') + 1:]
# print(a)

# Задача 2

# a = 'I am learning Python. hello, WORLD!'
# a = a[:a.find('h') + 1] + a[a.rfind('h') - 1:17:-1] + a[a.rfind('h'):]
# print(a)

# Задача 3

# a = input('-> ')
# old = input('Заменяемая подстрока: ')
# new = input('новая подстрока: ')
# a_new = a.replace(old, new)
# print(a_new)

# Задача 4

a = '''Ежевику для ежат
Пинесли два ежа.
Ежевику еле-еле
Ежата возле ели съели.'''
print(a, '\n', 'Количество слов: ', len(list(filter(lambda i: i[0] == "е", a.lower().split()))))

