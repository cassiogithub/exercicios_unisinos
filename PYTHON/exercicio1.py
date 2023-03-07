def dizer_ola(isExercício):
    if (isExercício):
        print('\nExercício I\n')

    nome = input("Digite seu nome\n")
    print(f'Olá {nome}')

def exercicio_dois():
    print('\nExercício II\n')
    nomeJogadorA = input('Digite o nome de  1 jogador:\n')
    idadeJogadorA = int(input('Digite a idade deste  jogador:\n'))

    nomeJogadorB = input('Digite o nome de  outro jogador\n')
    idadeJogadorB = int(input('Digite a idade deste  jogador\n'))

    if (idadeJogadorA > idadeJogadorA):
        print(f'Jogador mais velho é {nomeJogadorA}')
    elif (idadeJogadorB > idadeJogadorA):
        print(f'Jogador mais velho é {nomeJogadorB}')
    else:
        print('Ambos jogadores tem a mesma idade.')

def exercicio_tres():
    print('\nExercício III\n')
    dizer_ola(False)

    idadePessoa = int(input('Digite a sua idade:\n'))

    if(idadePessoa >= 18):
        print('Você é adulto\n')
    elif(idadePessoa < 18 and idadePessoa > 13):
        print('Você é adolescente\n')
    elif(idadePessoa >= 0 and idadePessoa <= 13):
        print('Você é criança\n')
    elif (idadePessoa < 0 ):
        print('Idade inválida\n')
    else:
        print('Idade inválida\n')

def exercicio_quatro():
    print('\nExercício IV\n')
    valorTotal = 0
    for i in range(4):
        numero = float(input('Digite um valor:\n'))
        valorTotal += numero

    if((valorTotal % 2) == 0):
        print('Valor par\n')
        return

    print('Valor Ímpar')
    return

def exercicio_cinco():
    print('\nExercício V\n')

    VALOR_DEFAULT = 0
    def verifica_negativo_positivo(valor):
        if valor > VALOR_DEFAULT:
            print('Valor é positvo\n')
        elif valor < VALOR_DEFAULT:
            print('Valor é negativo\n')
        elif valor == VALOR_DEFAULT:
            print(f'Valor é igual a {VALOR_DEFAULT}\n')
        else:
            print(f'Valor informado é inválido')

    for i in range(10):
        valor = int(input('Digite um valor:\n'))
        verifica_negativo_positivo(valor)



# PARA TESTAR EM CONSOLE AS FUNÇÕES DESCOMENTAR OS METODOS
# dizer_ola(True)
# exercicio_dois()
# exercicio_tres()
# exercicio_quatro()
# exercicio_cinco()