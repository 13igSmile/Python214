def numbers(lst):
    if not lst:
        return 0
    else:
        count = numbers(lst[1:])
        if lst[0] < 0:
            count += 1
        return count


print(numbers([-2, 3, 8, -11, -4, 6]))
