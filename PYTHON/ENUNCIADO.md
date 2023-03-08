# Exercício 1

Crie algoritmos para os problemas a seguir. Para cada algoritmo, crie uma representação em forma de FLUXOGRAMA.

1. Crie um algoritmo que solicita o nome do usuário pelo teclado e imprime na tela este nome.

2. Crie um algoritmo que pede o nome e a idade de dois jogadores (um de cada vez). Ao final, imprima o nome do jogador mais velho.

3. Crie um algoritmo que solicita o nome do usuário e a idade dele pelo teclado. O algoritmo deve imprimir na tela uma das mensagens abaixo:
- “Você é adulto”, quando a idade digitada for maior ou igual a 18
- “Você é adolescente”, quando a idade digitada for menor do que 18 e maior do que 13
- “Você é criança”, quando a idade digitada for maior ou igual a 0 e menor ou igual a 13
- “Idade inválida”, quando a idade digitada for menor do que 0

4. Crie um algoritmo que lê 4 números do teclado e imprime na tela se a soma dos 4 números é um valor par ou ímpar.

5. Crie um algoritmo que solicita que o usuário digite 10 números pelo teclado e, a cada número digitado, imprima na tela se o número é positivo, negativo ou zero.

# Exercício 2

Qual a diferença entre Linguagem de Máquina e Linguagem de Alto Nível?

Linguagem de máquina trata-se normalmente de um binário.
<br>
Linguagem de alto nível é a linguagem com a sintaxe aproximada da humana.

# Exercício 3

Quais são os dois principais processos de tradução de linguagens de alto nível para linguagem de máquina? Diferencie-os.

Compilação:
<p>
    Traduz a sintaxe de alto nivel para linguagem de máquina, assim verificando sintaxe e se há erros de codificação.
</p>
Interpretação:
<p>
    É um processo que o interpretador utilizado para ler o código le 1 linha e converte para o codigo de máquina.
</p>

# Exercício 4

Qual o tipo de dado dos valores abaixo?
- 7 - int
- "Casa" - string
- True - boolean
- -34 - int
- "876.90" - string
- 12 - int
- 23.1 - float
- -97.2 - float

# Exercício 5

Qual a linha de código para imprimir na tela a mensagem: "Hello, world!"?

em python: 

print('Hello, world!')

# Exercício 6

Pesquise sobre "precedência de operadores" e responda: o que será impresso no trecho de código abaixo?

x = 3+5*7
print(x)

será impresso o valor: 38

# Exercícío 7

Para cada situação abaixo, escreva um trecho de código para solicitar que o usuário digite tais dados e eles sejam armazenados na memória de forma correta (em relação ao tipo do dado):
- Solicitar o nome do usuário
- nome_usuario = input('Digite seu nome:')
- Solicitar a idade do usuário
- idade_usuario = int(input('Digite sua idade:'))
- Solicitar o peso do usuário
- peso_usuario = float(input('Digite sua idade:'))

# Exercício 8

Para os itens abaixo, crie o código solicitado:
- Solicitar ao usuário 2 valores inteiros e imprimir na tela o resultado da divisão de um pelo outro com 2 casas decimais.
- Solicitar ao usuário 2 valores inteiros e imprimir na tela o resultado da divisão de um pelo outro com 3 casas decimais.
- Solicitar ao usuário 2 valores inteiros e imprimir na tela o resultado da divisão de um pelo outro com 4 casas decimais.
```python
def exercicio_oito():
    valorA = int(input('Digite o valor A:'))
    valorB = int(input('Digite o valor B:'))
#    print(f'divisão: {valorA / valorB: .2f}')
    print(f'divisão: {divisao(valorA, valorB, 2)}')
    print(f'divisão: {divisao(valorA, valorB, 3)}')
    print(f'divisão: {divisao(valorA, valorB, 4)}')

def divisao(valorA, valorB, casasDecimais):
    return f'{valorA / valorB: .{casasDecimais}f}'

exercicio_oito()
```
