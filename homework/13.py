def decor(fn):
    def wrap(*args):
        print("Среднее арифметическое", fn(*args) / len(args))

    return wrap


@decor
def func(*args):
    print("Сумма:", sum(args))
    return sum(args)


func(2, 3, 3, 4)


