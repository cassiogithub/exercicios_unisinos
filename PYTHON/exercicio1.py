def dizer_ola(isExercicio):
    if (isExercicio):
        print('\nExercicio I\n')

    nome = input("Digite seu nome\n")
    print(f'Olá {nome}')


def exercicio_dois():
    print('\nExercicio II\n')
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
    print('\nExercicio III\n')
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

# dizer_ola(True)
# exercicio_dois()
# exercicio_tres()
