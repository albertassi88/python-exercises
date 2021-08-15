# Crie uma função que receba uma lista de nomes e retorne o nome com a maior
# quantidade de caracteres.

list_name = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def bigger_name(list_name):
    big_name = ''
    for name in list_name:
        if len(name) > len(big_name):
            big_name = name
    return big_name


print(bigger_name(list_name))
