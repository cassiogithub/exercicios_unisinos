import math


def exercicio_um():
    var_a = float(input('Digite o valor A: \n'))
    var_b = int(input('Digite o valor B: \n'))

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        return a / b

    def subtracao(a, b):
        return a - b

    def adicao(a, b):
        return a + b

    def elevacao(a, b):
        return a ** b

    print(f'A multiplcado por B é {multiplicacao(var_a, var_b)}')
    print(f'A dividido por B é {divisao(var_a, var_b)}')
    print(f'“A mais B é {adicao(var_a, var_b)} e A menos B é {subtracao(var_a, var_b)}')
    print(f'A elevado a B é {elevacao(var_a, var_b)}')


def exercicio_dois():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais.")
    else:
        raiz_quadrada = math.sqrt(delta)
        x1 = (-b + raiz_quadrada) / (2 * a)
        x2 = (-b - raiz_quadrada) / (2 * a)

        print(f"x' = {x1:.2f}; x'' = {x2:.2f}")


exercicio_um()
# exercicio_dois()
