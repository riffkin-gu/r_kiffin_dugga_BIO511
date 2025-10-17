numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

sum_abs = 0
for num in numbers:
    if abs(num) >= 10:
        sum_abs += num
        print(sum_abs)
print(f'Sum:{sum_abs}')


    