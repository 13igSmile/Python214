#   Задача 1

# a = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }
# print(a)
# a['emp3']['salary'] = 8500
# for i in a:
#     print(i, '\n', 'name :', a[i]['name'], '\n', 'salary :', a[i]['salary'])

#   Задача 2

s = {}
num = int(input("Кол-во студентов: "))
sum1 = 0
for i in range(num):
    name = input(str(i + 1) + "-й студент: ")
    points = int(input("Балл: "))
    s[name] = points
    sum1 += points
c = sum1 / num
print("Средний балл: ",  c, ". Студенты с баллом выше среднего: ")
for i in s:
    if s[i] > c:
        print(i)
