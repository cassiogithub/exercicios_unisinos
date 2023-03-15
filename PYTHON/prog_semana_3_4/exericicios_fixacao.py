def exericio_um():
    inteiro: int = int(input('Digite um valor inteiro'))
    if inteiro % 2 == 0:
        print('Par')
    elif inteiro % 2 != 0:
        print('Ímpar')
    else:
        print('Valor Inválido')


def exercicio_dois():
    valor_a: int = int(input('Digite um valor inteiro'))
    valor_b: int = int(input('Digite um valor inteiro'))
    if valor_b == 0:
        print('Erro na divisão por zero')
        return

    print(f'{valor_a / valor_b: .2f}')


def exercicio_tres():
    valor_a: int = int(input('Digite um valor inteiro'))
    if valor_a % 4 == 0:
        print('Ano bissexto')
        return

    print('Ano comum')


# exericio_um()
# exercicio_dois()
# exercicio_tres()