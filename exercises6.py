# Crie uma função que receba os três lado de um triângulo e informe qual o 
# tipo de triângulo formado ou "não é triangulo" , caso não seja possível
# formar um triângulo.


def triangle_type(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "não é triangulo"
    if side1 == side2 == side3:
        return "Triângulo Equilátero"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


print(triangle_type(10, 10, 10))
