# Calcule a média aritmética dos valores contidos em uma lista.

list_numbers = [10, 20, 30, 40]


def calculate_arithmetic_mean(list_numbers):
    sum = 0
    for number in list_numbers:
        sum += number
    return sum / len(list_numbers)


print(calculate_arithmetic_mean(list_numbers))
