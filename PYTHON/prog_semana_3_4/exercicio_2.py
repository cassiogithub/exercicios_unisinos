def qual_sexo(sexo: str) -> str:
    if sexo == 'F' and sexo == 'f':
        return 'sexo feminino'
    elif sexo == 'M' and sexo == 'm':
        return 'sexo masculino'
    return 'sexo invalido'

#Questão 1
# print(
#     qual_sexo('M'),
#     qual_sexo('f'),
#     qual_sexo('F'),
#     qual_sexo('m'),
#     qual_sexo('K'),
#     sep='\n')

# Questão 2
def questao_dois():
    x = "Até a pé nós iremos"
    for i in x:
        print(i)

# questao_dois()

def questao_quatro():
    i = 0
    while i < 100:
        i = i + 1
        if i == 50:
            break
    print(i)

# questao_quatro()

def questao_cinco(valor_z:int):
    z = valor_z
    while z != 10:
        if(z > 10):
            z = z - 1
        else:
            z = z + 1
    print(z)

questao_cinco(50)