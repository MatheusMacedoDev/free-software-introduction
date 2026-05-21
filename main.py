def sum_n_times(number, times):

    counter = 0
    sum = 0

    while counter < times:
        sum -= number
        counter += 1

    return sum

print(sum_n_times(4, 5))

