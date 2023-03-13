class Endereco:
    def __init__(self, logradouro, cep, bairro, cidade, estado):
        self.logradouro = logradouro
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


def exercicio_um(com_retorno: bool):
    nome_usuario = input('Digite seu nome: \n')

    if com_retorno is False:
        print(f'Seu nome é {nome_usuario}')
        return
    else:
        return nome_usuario


def exercicio_dois():
    nome_usuario = exercicio_um(True)
    idade_usuario = input('Digite sua idade: \n')
    print(f'Seu nome é {nome_usuario} e sua idade é {idade_usuario}\n')
    return


def exercicio_tres():
    exercicio_um(False)
    altura_usuario = float(input('Digite sua altura: \n'))
    print(f'Sua altura é {altura_usuario: .2f}\n')
    print('Obrigado pela sua parceria!')


def exercicio_quatro():
    nome_usuario = exercicio_um(True)
    endereco = Endereco(
        input('Digite o nome da sua rua:\n'),
        input('Digite seu CEP:\n'),
        input('Digite seu bairro:\n'),
        input('Digite sua cidade:\n'),
        input('Digite seu estado:\n')
    )

    print(f'Olá seu nome é: {nome_usuario} \n'
          f'Seu endereço é: {endereco.cidade}, no estado de(o/a) {endereco.estado} \n'
          f'Rua: {endereco.logradouro}, no CEP: {endereco.cep}')
    return


def exercicio_cinco():
    soma = 0
    produto = 1
    for i in range(5):
        valor_digitado = int(input('Digite um valor inteiro:'))
        soma += valor_digitado
        produto *= valor_digitado
    print(f'A soma dos produtos é: {soma}')
    print(f'O produto é: {produto}')


def exercicio_seis():
    a = int(input('Digite um valor inteiro:'))
    b = int(input('Digite um valor inteiro:'))
    c = int(input('Digite um valor inteiro:'))
    d = int(input('Digite um valor inteiro:'))
    e = int(input('Digite um valor inteiro:'))

    area_triangulo = (b * c) / 2
    print(f'Area de um triangulo {area_triangulo}')

    perimetro_retangulo = a + b + c + d
    print(f'Perímetro de um retângulo {perimetro_retangulo}')

    area_circulo = 3.14159 * e ** 2
    print(f'Area de círculo  {area_circulo}')


def exercicio_sete():
    nota_dez_porcento = float(input('Digite a nota que vale 10%: \n'))
    nota_trinta_porcento = float(input('Digite a nota que vale 30%: \n'))
    nota_sessenta_porcento = float(input('Digite a nota que vale 60%:: \n'))
    nota_final = (nota_dez_porcento * 0.1) + (nota_trinta_porcento * 0.3) + (nota_sessenta_porcento * 0.6)

    print(f'Sua nota final é: {nota_final}')


def calcula_grau_a(nota_pratica: float, nota_teorica: float) -> float:
    PORCENTAGEM_NOTA_TEORICA: float = 0.55
    PORCENTAGEM_NOTA_PRATICA: float = 0.45
    return (nota_teorica * PORCENTAGEM_NOTA_TEORICA) + (nota_pratica * PORCENTAGEM_NOTA_PRATICA)


def calcula_grau_b(nota_laboratorio: float, nota_teorica: float, nota_extraclasse: float) -> float:
    PORCENTAGEM_NOTA_LABORATORIO: float = 0.6
    PORCENTAGEM_NOTA_TEORICA: float = 0.2
    PORCENTAGEM_NOTA_EXTRACLASSE: float = 0.2
    return (nota_laboratorio * PORCENTAGEM_NOTA_LABORATORIO) + (nota_teorica * PORCENTAGEM_NOTA_TEORICA) + (
            nota_extraclasse * PORCENTAGEM_NOTA_EXTRACLASSE)


def calcula_nota_final(grau_a: float, grau_b: float) -> float:
    PORCENTAGEM_GRAU_A: float = 0.33
    PORCENTAGEM_GRAU_B: float = 0.67
    return (grau_a * PORCENTAGEM_GRAU_A) + (grau_b * PORCENTAGEM_GRAU_B)


def dados_grau_a() -> float:
    print('Olá, você digitará as notas equivalentes ao Grau A: \n')
    grau_a_pratica = float(input(f'Digite sua nota prática: \n'))
    grau_a_teorica = float(input(f'Digite sua nota teórica \n'))
    return calcula_grau_a(grau_a_pratica, grau_a_teorica)


def dados_grau_b() -> float:
    print('Obrigado, agora você digitará as notas equivalentes ao Grau B: \n')
    grau_b_laboratorio = float(input(f'Digite sua nota de laboratorio: \n'))
    grau_b_teorica = float(input(f'Digite sua nota teorica \n'))
    grau_b_extraclasse = float(input(f'Digite sua nota extraclasse \n'))
    return calcula_grau_b(grau_b_laboratorio, grau_b_teorica, grau_b_extraclasse)


def exercicio_oito():
    grau_a_final: float = dados_grau_a()
    grau_b_final: float = dados_grau_b()
    nota_final: float = calcula_nota_final(grau_a_final, grau_b_final)
    print(f'\nSua nota final é {nota_final}, parabéns! \n')


# exercicio_um(False)
# exercicio_dois()
# exercicio_tres()
# exercicio_quatro()
# exercicio_cinco()
# exercicio_seis()
# exercicio_sete()
exercicio_oito()
