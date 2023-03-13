class Endereco:
    def __init__(self, logradouro, cep, bairro, cidade, estado):
        self.logradouro = logradouro
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


def exercicio_um(com_retorno):
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


def exericio_seis():
    a = int(input('Digite um valor inteiro:'))
    b = int(input('Digite um valor inteiro:'))
    c = int(input('Digite um valor inteiro:'))
    d = int(input('Digite um valor inteiro:'))
    e = int(input('Digite um valor inteiro:'))

    area_triangulo = (b * c) / 2
    print(f'Area de um triangulo {area_triangulo}')

    perimetro_retangulo = a + b + c + d
    print(f'Perímetro de um retêngulo {perimetro_retangulo}')

    area_circulo = 3.14159 * e ** 2
    print(f'Area de círculo  {area_circulo}')


def exercicio_sete():
    nota_dez_porcento = float(input('Digite a nota que vale 10%: \n'))
    nota_trinta_porcento = float(input('Digite a nota que vale 30%: \n'))
    nota_sessenta_porcento = float(input('Digite a nota que vale 60%:: \n'))

    nota_final = (nota_dez_porcento * 0.1) + (nota_trinta_porcento * 0.3) + (nota_sessenta_porcento * 0.6)

    print(f'Sua nota final é: {nota_final}')
# exercicio_um(False)
# exercicio_dois()
# exercicio_tres()
# exercicio_quatro()
# exercicio_cinco()
# exericio_seis()
# exercicio_sete()
