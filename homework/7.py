a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
b = []
c = []
for i in a:
    for j in range(2, i):
        if i % j == 0:
            c.append(i)
        else:
            b.append(i)
print("Min: ", min(b))
print("Max: ", max(c))
