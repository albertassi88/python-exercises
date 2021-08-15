# Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na
# tela um quadrado feito de asteriscos de lado de tamanho n.

n = 4

# exemplo 1
def print_asterisks(numbers):
    for number in range(numbers):
        count = ""
        for number in range(numbers):
            count += "*"
        print(count)


print(print_asterisks(n))


# exemplo 2
def draw_square(n):
    for row in range(n):
        print(n * "*")


print(draw_square(n))
