lst = [1, 2, 3, 4, 5, 8, 9, 0, 100, 23, 4, 12, 237, 10, 12, 14, 15]

for number in lst:
    if number % 2 == 0:
        print(number , end='')
    elif number == 237:
        break
