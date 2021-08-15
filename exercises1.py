# Crie uma função que receba dois números e retorne o maior deles.

def returns_the_largest_number(number_one, number_two):
    if number_one > number_two:
        return number_one
    else:
        return number_two


print(returns_the_largest_number(50, 100))
