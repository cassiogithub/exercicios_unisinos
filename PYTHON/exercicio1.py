def dizer_ola(is_exercicio):
    if is_exercicio:
        print('\nExercício I\n')

    nome = input("Digite seu nome\n")
    print(f'Olá {nome}')


def exercicio_dois():
    print('\nExercício II\n')
    nome_jogador_a = input('Digite o nome de  1 jogador:\n')
    idade_jogador_a = int(input('Digite a idade deste  jogador:\n'))

    nome_jogador_b = input('Digite o nome de  outro jogador\n')
    idade_jogador_b = int(input('Digite a idade deste  jogador\n'))

    if idade_jogador_a > idade_jogador_a:
        print(f'Jogador mais velho é {nome_jogador_a}')
    elif idade_jogador_b > idade_jogador_a:
        print(f'Jogador mais velho é {nome_jogador_b}')
    else:
        print('Ambos jogadores tem a mesma idade.')


def exercicio_tres():
    print('\nExercício III\n')
    dizer_ola(False)

    idade_pessoa = int(input('Digite a sua idade:\n'))

    if idade_pessoa >= 18:
        print('Você é adulto\n')
    elif 18 > idade_pessoa > 13:
        print('Você é adolescente\n')
    elif 0 <= idade_pessoa <= 13:
        print('Você é criança\n')
    elif idade_pessoa < 0:
        print('Idade inválida\n')
    else:
        print('Idade inválida\n')


def exercicio_quatro():
    print('\nExercício IV\n')
    valor_total = 0
    for i in range(4):
        numero = float(input('Digite um valor:\n'))
        valor_total += numero

    if (valor_total % 2) == 0:
        print('Valor par\n')
        return

    print('Valor Ímpar')
    return


def exercicio_cinco():
    print('\nExercício V\n')

    VALOR_DEFAULT = 0

    def verifica_negativo_positivo(valor_recebido):
        if valor_recebido > VALOR_DEFAULT:
            print('Valor é positvo\n')
        elif valor_recebido < VALOR_DEFAULT:
            print('Valor é negativo\n')
        elif valor_recebido == VALOR_DEFAULT:
            print(f'Valor é igual a {VALOR_DEFAULT}\n')
        else:
            print(f'Valor informado é inválido')

    for i in range(10):
        valor = int(input('Digite um valor:\n'))
        verifica_negativo_positivo(valor)

def exericio_oito():
    valorA = int(input('Digite o valor A:'))
    valorB = int(input('Digite o valor B:'))
    print(f'divisão: {divisao(valorA, valorB, 2)}')
    print(f'divisão: {divisao(valorA, valorB, 3)}')
    print(f'divisão: {divisao(valorA, valorB, 4)}')

def divisao(valorA, valorB, casasDecimais):
    return f'{valorA / valorB: .{casasDecimais}f}'

# PARA TESTAR EM CONSOLE AS FUNÇÕES DESCOMENTAR OS METODOS
# dizer_ola(True)
# exercicio_dois()
# exercicio_tres()
# exercicio_quatro()
# exercicio_cinco()
# exericio_oito()