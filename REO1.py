# VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS- REO1
# NOME: Caroline Marcela da Silva.
# GITHUB: CarolineMSilva

########################################################################################################################
########################################################################################################################

##### Pacotes utilizado #####

""" ANOTAÇÕES

Numpy- É um pacote que permite realizar operações básicas com coleções- arrays, vetores e matrizes multidimensionais.
 Esse pacote foi instalado pelo pip e precisa ser importado para sua utilização.

Matplotlib- É uma biblioteca do python para a elaboração de gráficos."""

# Instalação
import numpy as np

# Para importar a biblioteca matplotlib
from matplotlib import pyplot as plt

########################################################################################################################
########################################################################################################################

##### EXERCÍCIO 01 #####'

print('Exercício 1')
print(' ')

# Questão A

print('a- Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Primeiramente, vou criar uma lista com os valores pedidos. Em seguida, irei transformar essa lista em um array 
para o numpy, através de um vetor. Em seguida, chamei a função print para confirmar o tipo do vetor criado."""

print('RESPOSTA')
print(' ')

lista=[3.5,150.30,17,28,35,79,20,99.07,15]
print('Lista:{}'.format(lista))

vetor= np.array(lista)
print('Vetor:{}'.format(vetor))
print('Tipo do vetor:')
print(type(vetor))

print('------------------------------------------------------------------------------------------')
print(' ')

#######################################################################################################################

# Questão B

print('b- Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para obter essas informações, irei usar diferentes funções, tanto do numpy, quanto do próprio python. A dimensão do 
vetor pode ser dada pelo função len do python ou pela função np.shape do numpy. Para a caracterizar valor máx e mín usei
essas respectivas funções do python. E para finalizar, a média e a variância foram obtidas com as funções np.mean e np.var
do numpy.
Obs.:Quando a dimensão é obtida pela função np.shape do numpy, o tipo da variável que sai é uma Tupla (um tipo imutável 
e tem seus elementos delimitados por parênteses)."""

print('RESPOSTA')
print(' ')

print('Dimensão do vetor: {}'.format(len(vetor)))
print('Dimensão do vetor com função do numpy: {}'.format(np.shape(vetor)))
print('Média do vetor: {}'.format(np.mean(vetor)))
print('Valor máximo do vetor: {}'.format(max(vetor)))
print('Valor mínimo do vetor: {}'.format(min(vetor)))
print('Variância do vetor: {}'.format(np.var(vetor)))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão C

print('c- Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor'
      ' declarado a letra a e o valor da média deste.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para isso, vou criar uma variavél (x) que abriga a média de todos os elementos do vetor original. Em seguida, criar um 
novo vetor (vetor1), dessa vez, com duas operações, primeiro a subtração dos valores do vetor e sua média, e segundo, o 
quadrado do resultado, seguindo a ordem de precedência dos operadores, em que primeiro se resolve o que está entre 
parênteses e depois potência."""

print('RESPOSTA')
print(' ')

x = np.mean(vetor)
print('A média dos vetores é: {}'.format(x))
vetor1 = ((vetor-x)**2)
print('O vetor1 apresenta os elementos:{}'.format(vetor1))
print('Tipo do vetor:')
print(type(vetor1))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão D

print('d- Obtenha um novo vetor que contenha todos os valores superiores a 30.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Vou criar um novo vetor (vetor2), que irá abrigar somente os valores maiores que 30 que existem no vetor original."""

print('RESPOSTA')
print(' ')

vetor2= (vetor[vetor>30])
print('O vetor2 apresenta os elementos:{}'.format(vetor2))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão E

print('e- Identifique quais as posições do vetor original possuem valores superiores a 30.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para isso, vou aplicar a função np.where do numpy no vetor original, criando a variável pos, de posição."""

print('RESPOSTA')
print(' ')

pos= np.where(vetor>30)
print('Posições dos elementos maiores que 30: {}'.format(pos))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão F

print('f- Apresente um vetor que contenha os valores da primeira, quinta e última posição.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Vou criar um vetor com esses elementos, tendo atenção para a indicação das posições, visto  que a contagem inicia-se a
partir de 0, e o último valor pode ser representado por -1. Dessa forma o primeiro número será posição 0, e as posições
serão sempre o seu valor - 1."""

print('RESPOSTA')
print(' ')

vetor3= (vetor[0], vetor[4], vetor[-1])
print('O vetor contendo os elementos da primeira, quinta e última posição é: {}'.format(vetor3))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão G

print('g- Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as '
      'iterações')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Estrutura de repetição for -> for (variavel) in (lista/vetor)
A variável recebe cada um dos elementos da lista, é aplicada a eles, repetidamente, em forma de loop contínuo.
Para identificar, pelo comando print, tudo que tem dentro do for, é preciso usar identação (espaço antes do paragráfo),
de forma que fique indentado tudo que está dentro da estrutura for.
A função enumerate permite associar duas variáveis a estrutura de repetição, capturando a posição e o valor de cada 
elemento, por exemplo.
A iteração é como se fosse cada passo da rodada, e sempre se inicia com 0."""

print('RESPOSTA')
print(' ')

it = 0
for pos,valor in enumerate(vetor):
    it = it+1
    print('Iteração {} --> Na posição {} ocorre o valor {}'.format(it, pos, valor))
    print('-------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------')
print(' ')

#######################################################################################################################

# Questão H

print('h- Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Primeiro, criar uma função  para a soma dos quadrados, a partir do comando def. Tudo que vai ser executado dentro
da função exige identação. 
Somador recebe zero porque é o ponto inicial, é uma variável ao qual vai ser somada os elementos do vetor. Funciona 
também na estrutura de loop. Sempre vai ser somado ao valor anterior. Como vai precisar acessar os valores 1 por vez, 
vai ser necessário criar a estrutura de repetição. 
O for vai estar dentro da função e por isso com identação. For, variável elemento, dentro do vetor. Como ele quer soma 
de quadrados, o somador vai ser o resultado de cada etapa, mais o elemento elevado ao quadrado. Como o somador começa 
com zero e no próximo ciclo, ele vai ser o resultado do anterior ja elevado ao quadrado, não precisa elevar ele na função. 
Instrução Return-> toda função tem uma resposta, e usa essa pra retornar a resposta do somatório de todos os valores do 
vetor. Por fim, chama a função criada e informa o vetor a ser utilizado."""

print('RESPOSTA')
print(' ')

def somadosquadrados (vetor):
    somador = 0
    it = 0
    for elem in vetor:
        print('Elemento: {}'.format(elem))
        print('Somador: {}'.format(somador))
        somador = somador + elem**2
        it = it + 1
        print('Iteração {} - Somatório: {}'.format(it, somador))
        print('---------------------------------------------------------------------------------')
    return somador
print(vetor)
somadosquadrados(vetor)

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão I

print('i- Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Estrutura de repetição  While, depende de uma determinada condição na sua estrutura. 
Você determina um parãmetro que é verdadeiro, no caso pos=0, de posição.
Também precisa de identação. Então, é assim: Determino uma condição, enquanto a variavel 
for diferente da condição, executa as instruções que seguem. Se for diferente, a cada iteração vai ser adicionado 1. 
Quando a pos for igual a dimensão do vetor, a condição vai ser falsa e vai desabilitar o loop."""

print('RESPOSTA')
print(' ')

print('Será realizado uma contagem até que o valor apresentado seja diferente de 8, começando pelo 0:')
pos = 0
while vetor[pos] != 8:
    print(vetor[pos])
    pos = pos+1
    if pos==(len(vetor)):
        print('Posição igual a {}, condição estabelecida de posição passa a ser true, e a função é desabilitada.'.format(pos))
        break

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão J

print('j- Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para criar uma sequência do mesmo tamanho do vetor usa-se a função range e especifica a sequencia de valores que vc 
quer que inicia, no caso 1, o valor final, que vai ser a dimensão do vetor original, no caso +1, porque tem que ter o 
mesmo tamanho, e como se inicia em 1, perderia 1 unidade, e o passo que deseja entre os números, no caso 1 também"""

print('RESPOSTA')
print(' ')

vetor4=list(range(1, len(vetor)+1, 1))
print('Sequência de valores: {}'.format(vetor4))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão K

print('k- Concatene o vetor da letra a com o vetor da letra j.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para concatenar, basta usar a função do numpy np.concatenate"""

print('RESPOSTA')
print(' ')

concatenação = np.concatenate((vetor, vetor4), axis=0)
print(concatenação)

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################
########################################################################################################################

##### EXERCÍCIO 02 #####

print('Exercício 2')
print(' ')

# Questão A

print('a- Declare a matriz com a biblioteca numpy.')
print(' ')

# 1 3 22
# 2 8 18
# 3 4 22
# 4 1 23
# 5 2 52
# 6 2 18
# 7 2 25

"""ANOTAÇÕES SOBRE A QUESTÃO

Para declarar uma matriz, também se utiliza a função np.array. Entretanto, além dos parenteses, utiliza-se colchetes 
para indicar as linhas. É importante que dois colchetes também delimite toda a matriz do início ao fim. Vírgulas separam 
as linhas. Pode separar em linhas diferentes, fica melhor pra observar e não atrapalha a função."""

print('RESPOSTA')
print(' ')

matriz = np.array([[1, 3, 22],
                   [2, 8, 18],
                   [3, 4, 22],
                   [4, 1, 23],
                   [5, 2, 52],
                   [6, 2, 18],
                   [7, 2, 25]])
print(matriz)

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão B

print('b- Obtenha o número de linhas e de colunas desta matriz.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para matrizes, ao invés da função len do python para determinar a dimensão, nós utilizamos a função do numpy np.shape.
Para isso criei duas variáveis, nl, número de linhas e nc, número de colunas e apliquei a função na matriz"""

print('RESPOSTA')
print(' ')

nl, nc = np.shape(matriz)
print('A matriz apresenta {} linhas.'.format(nl))
print('A matriz apresenta {} colunas.'.format(nc))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão C

print('c- Obtenha as médias das colunas 2 e 3.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para obter a média de apenas algumas colunas específicas da matriz, irei criar duas variáveis/submatrizes, chamadas
coluna2 e coluna3, que vai abrigar somente a parte de interesse, no caso, a coluna 2 e a coluna 3, respectivamente.
Depois aplicar a fução np.mean ou np.average em ambas as variáveis ou submatrizes.
obs.: Novamente, ter atenção com as posições de linhas e colunas, pois elas também se iniciam em 0, assim, para acessar 
a coluna 2 vou indicar na função que ela está na posição 1, por exemplo.
Dentro da função, separa-se as linhas da coluna por vírgula e o símbolo : indica que é pra usar todas as linhas ou colunas
respectivamente."""

print('RESPOSTA')
print(' ')

coluna2 = matriz[:,1]
mediacoluna2 = np.mean(coluna2)
print('A média da coluna 2 da matriz original é {}'.format(mediacoluna2))
print('----------------------------------------------------------------')

coluna3 = matriz[:,-1]
mediacoluna3 = np.mean(coluna3)
print('A média da coluna 3 da matriz original é {}'.format(mediacoluna3))
print('----------------------------------------------------------------')

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão D

print('d- Obtenha as médias das linhas considerando somente as colunas 2 e 3.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

O raciocíneo é o mesmo do feito anteriormente para as colunas 2 e 3.
A diferença é que ao criar a variável, vou indicar separadamente as linhas e as colunas, em chaves difentes.
E novamente, tirar a média de cada variável.
OBS: Uma outra maneira de fazer o script é criar uma submatriz só com as colunas 2 e 3 e suas linhas. Assim na hora de 
explicar a matriz não precisaria usar dois colchetes para indicar as linhas e a coluna, e sim indicaria somente as 
linhas, ex. matriz(0,:)"""

print('RESPOSTA')
print(' ')

linha1 = matriz[0,[1,2]]
medialinha1 = np.mean(linha1)
print('A média da linha 1, considerando as colunas 2 e 3, é {}'.format(medialinha1))
print('-------------------------------------------------------------------------')

linha2 = matriz[1,[1,2]]
medialinha2 = np.mean(linha2)
print('A média da linha 2, considerando as colunas 2 e 3, é {}'.format(medialinha2))
print('-------------------------------------------------------------------------')

linha3 = matriz[2,[1,2]]
medialinha3 = np.mean(linha3)
print('A média da linha 3, considerando as colunas 2 e 3, é {}'.format(medialinha3))
print('-------------------------------------------------------------------------')

linha4 = matriz[3,[1,2]]
medialinha4 = np.mean(linha4)
print('A média da linha 4, considerando as colunas 2 e 3, é {}'.format(medialinha4))
print('-------------------------------------------------------------------------')

linha5 = matriz[4,[1,2]]
medialinha5 = np.mean(linha5)
print('A média da linha 5, considerando as colunas 2 e 3, é {}'.format(medialinha5))
print('-------------------------------------------------------------------------')

linha6 = matriz[5,[1,2]]
medialinha6 = np.mean(linha6)
print('A média da linha 6, considerando as colunas 2 e 3, é {}'.format(medialinha6))
print('-------------------------------------------------------------------------')

linha7 = matriz[6,[1,2]]
medialinha7 = np.mean(linha7)
print('A média da linha 7, considerando as colunas 2 e 3, é {}'.format(medialinha7))
print('-------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão E

print('e- Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma'
'doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para resolver essa questão, vou criar uma variável (c2) somente com a coluna 2, que é a equivalente as notas de 
severidade da doença, visualizar, e depois utilizar a função np.where para localizar as notas menores que 5.
E a partir dai, crio uma outra variável para a coluna 1 (c1) e cruzo as informações das posições com os genòtipos"""

print('RESPOSTA')
print(' ')

c2 = (matriz[:, 1])
print('As notas de severidade dos genótipos são: {} '.format(c2))
notas_menor5 = np.where(c2<5)
print('As posições na matriz dos genótipos que possuem notas inferiores a 5 são: {}'.format(notas_menor5))
c1 = (matriz[:,0])
gen_notas_menor5 = c1[notas_menor5]
print('Os genótipos com notas inferiores a 5 são: {} '.format(gen_notas_menor5))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão F

print('f- Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma'
'doença e  a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

O raciocinio é o mesmo para a questão anterior."""

print('RESPOSTA')
print(' ')

c3 = (matriz[:, -1])
peso_maior_igual22 = np.where(c3>=22)
print('As posições na matriz dos genótipos que possuem peso de 100 grãos igual ou superior a 22 são: {}'.format(peso_maior_igual22))
c1 = (matriz[:, 0])
gen_peso_maior_igual22 = c1[peso_maior_igual22]
print('Os genótipos com peso de 100 grãos igual ou superior a 22: {}'.format(gen_peso_maior_igual22))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão G

print('g- Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e'
'e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100'
'grãos igual ou superior a 22.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para obter a nota, fiz o mesmo esquema da questão F, criando uma variável, aplicando a função, tranformando para bol.
Imprimi o resultado para notas, e o resultado para peso dos grãos, que foi obtido na questão anterior.
Depois criei um vetor associando o valor boleano das duas variaveis em suas respectivas colunas, com a coluna 1, que tem a identidade dos 
genótipos, através do &. Como os resultados eram duas tuplas, foi preciso transformar para bol"""

print('RESPOSTA')
print(' ')

notas_menor3 = np.where(c2<=3)
print('As posições na matriz dos genótipos que possuem notas inferiores a 3 são: {}'.format(notas_menor3))
bol_menor3 = c2<=3
print('Transformando para valor boleano: {}'.format(bol_menor3))
c1 = (matriz[:,0])
gen_notas_menor3 = c1[bol_menor3]
print('Os genótipos com notas inferiores a 3 são: {} '.format(gen_notas_menor3))

bol_peso_maior_igual22 = c3>=22
gen_peso_maior_igual22 = c1[bol_peso_maior_igual22]
print('Os genótipos com peso de 100 grãos igual ou superior a 22: {}'.format(gen_peso_maior_igual22))

gen_nota3peso22 = c1[bol_menor3 & bol_peso_maior_igual22]
print('Os genótipos com nota de severidade de doença inferior ou igual a 3 e peso de 100 grãos superior ou igual a 22 são: {}'.format(gen_nota3peso22))

print('------------------------------------------------------------------------------------------')
print(' ')


########################################################################################################################

# Questão H

print('h- Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu'
      'respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido.'
      'Apresente a seguinte mensagem a cada iteração "Na linha X e na coluna Y ocorre o valor: Z".'
      'Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

A príncipio chamei a matriz, número de linhas e colunas, de modo a visualizar novamente.
A cada iteração vou acessar um elemento da matriz, passando por todas as suas posições. Então, a estrutura for vai ter que 
dar tanto a posição de linha quanto a de coluna de cada um desses elementos. Dessa forma será preciso criar duas estruturas 
for, que irão atuar de modo integrado, uma para linha e outra para coluna, i e j. Então for para variável i que recebe 
uma lista, que varia de 0 até o número de linhas (nl), ao passo de 1. O mesmo raciocinio se aplica ao for de colunas,j.
O contador é o iterador e vai ser igual a 0, aumentando de um em um a cada passo.
Ao final da questão ele pede para criar uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25.
Para isso, criei uma estrutura de condição if.. então quando tiver passando por cada posição das linhas, se o valor do peso
for igual ou superior a 25, ele vai salvar em um arranjo criado na variável genotipo, pela função .append."""

print('RESPOSTA')
print(' ')

nl, nc = np.shape(matriz)
print(matriz)
print('Número de Linhas: {}'.format(nl))
print('Número de Colunas: {}'.format(nc))
print(' ')

contador = 0
genotipo = []
for i in np.arange(0,nl,1):
    if matriz[i, 2] >= 25:
        genotipo.append(matriz[i, 0])
    for j in np.arange(0,nc,1):
        contador = contador + 1
        print('Iteração {} --> Na linha {} e na coluna {} ocorre o valor {}'.format(contador, i, j, matriz[int(i),int(j)]))
print(' ')
print("A partir destes dados, os genótipos com peso de 100 grãos iguais ou superiores a 25 foram: {}".format(genotipo))
print(' ')

########################################################################################################################
########################################################################################################################

##### EXERCÍCIO 03 #####

print('Exercício 3')
print(' ')

# Questão A

print('a- Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor'
      ' qualquer, baseada em um loop (for). ')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Vou importar a função criada em outro arquivo python, declarar um vetor qualquer e testar as funções.
Para importar vou usa from + nome do arquivo + import + funções criadas."""

print('RESPOSTA')
print(' ')

from funções_questão3a_reo1 import media, variancia_amostral

vetor_teste = np.array([10,20,30,40,50])
print('Vetor:{}'.format(vetor_teste))

m= media(vetor_teste)
print('A média do vetor é: {}'.format(m))

v= variancia_amostral(vetor_teste)
print('A variância do vetor é: {}'.format(v))
print(' ')

########################################################################################################################

# Questão B

print('b- Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 e'
      ' variância 2500. Pesquise na documentação do numpy por funções de simulação.')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Para simular o array, aleatoriamente, com distribuição normal vou usar a função np.ramdom.normal.
Ao usar essa função, é preciso fornecer 3 argumentos, média, desvio padrão e o tamanho do vetor a ser criado.
Como na questão pede a mesma média e a mesma variância, vou criar uma variável para elas.
A função pede desvio padrão, e esse é a raiz quadrada da variancia, portanto, vou usar o valor 50, ao invés de 2500."""

print('RESPOSTA')
print(' ')

med, sigma = 100, 50
vetor_10 = np.random.normal(med,sigma,10)
#print('Vetor com 10 elementos: {}'.format(vetor_10))
print(' ')
vetor_100 = np.random.normal(med,sigma,100)
#print('Vetor com 100 elementos: {}'.format(vetor_100))
print(' ')
vetor_1000 = np.random.normal(med,sigma,1000)
#print('Vetor com 1000 elementos: {}'.format(vetor_1000))
print(' ')

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão C

print('c- Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b. ')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

Criei variáveis aplicando as funções nos vetores, e usei o print para imprimi-las"""

print('RESPOSTA')
print(' ')

m1= media(vetor_10)
v1= variancia_amostral(vetor_10)
print('A média do vetor_10 é {}. A variância do vetor é {}'.format(m1,v1))
print(' ')

m2= media(vetor_100)
v2= variancia_amostral(vetor_100)
print('A média do vetor_100 é {}. A variância do vetor é {}'.format(m2,v2))
print(' ')

m3= media(vetor_1000)
v3= variancia_amostral(vetor_1000)
print('A média do vetor_1000 é {}. A variância do vetor é {}'.format(m3,v3))
print(' ')

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão D

print('d- Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000. ')
print(' ')


"""ANOTAÇÕES SOBRE A QUESTÃO

Primeira coisa: Vou criar o vetor de 10000.
Em seguida, fazer os gráficos com a biblioteca matplotlib"""

print('RESPOSTA')
print(' ')

# Para criar vetor com 100000 elementos
med, sigma = 100, 50
vetor_100000 = np.random.normal(med,sigma,100000)
#print('Vetor com 100000 elementos: {}'.format(vetor_100000))
print(' ')

# Gráficos

plt.style.use('dark_background')                    #estilo gráfico- fundo escuro
fig, axs = plt.subplots(nrows=2, ncols=2)           #figura com 4 eixos, duas linhas e duas colunas, comando para colocar mais de um gráfico em uma figura.
ax0, ax1, ax2, ax3 = axs.flatten()                  #ordem dos gráficos nos eixos

# vetor 10 elementos
ax0.hist(vetor_10, color="tab:blue")                #comando para plotar o gráfico para o primeiro vetor, e cor
ax0.set_title('10 elementos')                       #título

#vetor 100 elementos
ax1.hist(vetor_100, color="tab:purple")
ax1.set_title('100 elementos')

#vetor 1000 elementos
ax2.hist(vetor_1000, color="tab:pink")
ax2.set_title('1000 elementos')

#vetor 100000 elementos
ax3.hist(vetor_100000, color="tab:brown")
ax3.set_title('100000 elementos')

fig.tight_layout()                                  #Ajuste dos subquadrantes para fornecer preenchimento sem sobreposição
plt.show()                                          #mostrar o gráfico

########################################################################################################################
########################################################################################################################

##### EXERCÍCIO 04 #####

print('Exercício 4')
print(' ')

# Questão A

print('a- O arquivo dados.txt contém a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a '
      'quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, '
      'apresente os dados e obtenha as informações de dimensão desta matriz. ')
print(' ')

"""ANOTAÇÕES SOBRE A QUESTÃO

1- Coloquei o arquivo dados txt na pasta do meu projeto no pycharm, no meu computador. A partir daí preciso chamar 
os dados pela função p.loadtxt do numpy. Criei uma variável para receber esses dados.
2- Em seguida, apliquei a função np.shape para obter o numero de linhas e numero de colunas, criando duas variáveis para 
abrigar essas informações."""

print('RESPOSTA')
print(' ')

dados = np.loadtxt('dados.txt')
print('Avaliação dos genótipos:')
print(' ')
print('   Gen    Rep     V1     V2     V3     V4     V5')
print(dados)
print(' ')

nl_dados, nc_dados = np.shape(dados)
print('Número de linhas: {}'.format(nl_dados))
print('Número de colunas: {}'.format(nc_dados))
print(' ')

########################################################################################################################

# Questão B

print('b- Pesquise sobre as funções np.unique e np.where da biblioteca numpy')
print(' ')

""" ANOTAÇÕES DA QUESTÃO
NP.UNIQUE
    A função np.unique retorna os elementos exclusivos classificados de acordo com determinada condição de uma matriz.
Existem três saídas opcionais, além dos elementos exclusivos:

1- os índices da matriz de entrada que fornecem valores únicos
2- os índices da matriz exclusiva que reconstroem a matriz de entrada
3- o número de vezes que cada valor exclusivo aparece na matriz de entrada.
-----###-------
NP.WHERE
    A função np.where permite localizar qualquer posição em um array numpy de acordo com uma condição que nós determinamos,
por exemplo, como utilizamos em outras questões, para encontrar posições no vetor em que os valores são menores que 5 (condição).
Se as variáveis forem especificadas, a função pode nos retornar a resposta como True ou False (tipo boleano), quanddo só
a condição for especificada, ela  nos devolve o tipo Tupla."""

print('RESPOSTA')
print(' ')

#help(np.unique)
#print(' ')
#help(np.where)

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão C

print('c- Obtenha de forma automática os genótipos e quantas repetições foram avaliadas ')
print(' ')

"""ANOTAÇÕES DA QUESTÃO

Apliquei a função unique nas duas primeiras coluas, criando uma variável para cada. A função unique seleciona os elementos
diferentes em cada coluna"""

print('RESPOSTA')
print(' ')

genotipos_dados= np.unique(dados[:,0])
repeticoes_dados= np.unique(dados[:,1])
print(" Os genótipos são {}, e cada um deles apresentam as repetições {}.".format(genotipos_dados,repeticoes_dados))

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão D

print('d- Apresente uma matriz contendo somente as colunas 1, 2 e 4.')
print(' ')

"""ANOTAÇÕES DA QUESTÃO

Vou criar uma submatriz, contendo todas as linhas e as colunas de posição 0,1 e 3."""

print('RESPOSTA')
print(' ')

submatriz_dados= dados[:,[0,1,3]]
print('Matriz contendo somente as colunas 1,2 e 4:')
print(submatriz_dados)

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão E

print('e- Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da'
      ' coluna 4. Salve esta matriz em bloco de notas. ')
print(' ')

"""ANOTAÇÕES DA QUESTÃO

1- Utilizei a submatriz da questão anterior.
2- Criei uma variável, para abrigar a nova matriz (np.zeros). Essa vai ter a dimensão de 5 posições. Dessas 5, eu to copiando a 
primeira coluna dos genótipos, de modo que fique unificado as repetições.
3- Vou criar um loop com o for para gerar os dados de cada genótipo, de acordo com suas repetições.
4- o it vai ser os genótipos, a cada rodada vai somar 1.
5- Para max e min, usei as funções do np. aplicadas a posição 0 da minha matriz, associando com a coluna 3. A cada ciclo 
a variavel n, vai aumentando 1 (por exemplo, no segundo ciclo 1+1= genotipo 2(variável).
6- Na média e variância, usei a função np.around para formatar a quantidade de casas. A lógica da interpretação é a mesma
do max e min.
7- Para salvar, np.savetxt."""

print('RESPOSTA')
print(' ')

submatriz_dados= dados[:,[0,1,3]]
matriz_gerada = np.zeros((len(np.unique(submatriz_dados[:, 0])), 5))
it = 0
for n in range(0, len(np.unique(submatriz_dados[:, 0])), 1):
    it = it + 1
    print(' ')
    print('Genótipo: {}'.format(it))
    print('Máxima: {}'.format(np.max((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])))
    print('Mínimo: {}'.format(np.min((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])))
    print('Média: {}'.format((np.around(np.mean((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3))))
    print('Variância: {}'.format((np.around(np.var((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3))))
    matriz_gerada[n, 0] = n + 1
    matriz_gerada[n, 1] = np.max((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])
    matriz_gerada[n, 2] = np.min((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])
    matriz_gerada[n, 3] = np.around(np.mean((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3)
    matriz_gerada[n, 4] = np.around(np.var((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3)
    print('------------------------------------------------------------------------------------------------------')
np.savetxt('Matriz_gerada_questão4_Reo1.txt', matriz_gerada)
print(' ')
print('Matriz Gerada --> Genótipo, Máxima, Mínima, Média e Variância')
print(matriz_gerada)

print('------------------------------------------------------------------------------------------')
print(' ')

########################################################################################################################

# Questão F

print('f-Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.')
print(' ')

"""ANOTAÇÕES DA QUESTÃO

1-Na matriz elaborada na questão anterior, selecionei na coluna 4, das médias, os valores boleanos maiores igual a 500.
2-Criei uma variável com a coluna dos genótipos da matriz.
3- Relacionei os valores boleanos com a coluna de genótipos."""

print('RESPOSTA')
print(' ')

media_maior_igual_500= matriz_gerada[:,3]>=500
coluna0= matriz_gerada[:,0]
genotipo_maior_igual_500= coluna0[media_maior_igual_500]
print('Os genótipos que apresentam média maior e igual a 500 são: {}'.format(genotipo_maior_igual_500))

print('------------------------------------------------------------------------------------------')
print(' ')


########################################################################################################################

# Questão G

print('g- Apresente os seguintes graficos: ')
print(' ')

#Gráfico das médias

print('Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura')
print(' ')

"""ANOTAÇÕES DA QUESTÃO

- São 5 variáveis no vetor original, então vou criar 5 variaveis para abrigar matriz de cada coluna, para a média.
Com a estrutura for, criei uma matriz das médias de cada genótipo para as 5 variáveis."""

print('RESPOSTA')
print(' ')

media_v1 = np.zeros((10,1))               # criei um vetor de zeros com 10 linhas e 1 coluna
media_v2 = np.zeros((10,1))
media_v3 = np.zeros((10,1))
media_v4 = np.zeros((10,1))
media_v5 = np.zeros((10,1))
contador = 0
for i in np.arange(0,30,3):             #percorre as 30 linhas do vetor original de acordo com o numero de repetições
    media_v1[contador,0] = np.mean(dados[i:i + 3, 2], axis=0)
    media_v2[contador,0] = np.mean(dados[i:i + 3, 3], axis=0)
    media_v3[contador,0] = np.mean(dados[i:i + 3, 4], axis=0)       #média dos dados, acessando as três rep de cada genót.
    media_v4[contador,0] = np.mean(dados[i:i + 3, 5], axis=0)
    media_v5[contador,0] = np.mean(dados[i:i + 3, 6], axis=0)
    contador = contador + 1
genotipos = np.unique(dados[0:30,0:1], axis=0)
medias_variaveis = np.concatenate((genotipos, media_v1, media_v2, media_v3, media_v4, media_v5), axis=1)  #matriz com as medias dos genotipos p as 5 var Axis= 1organiza as 5 colunas.. se for igual a 0, fica meio que empilhado
print('As médias das variáveis são:')
print(medias_variaveis)
print(' ')


plt.style.use('ggplot')
fig = plt.figure('Gráfico de Médias')

#Variável 1

plt.subplot(2,3,1)                          # dimensão da figura, duas linhas, tres colunas, posição que o primeiro gráfico vai ocupar.
plt.bar(medias_variaveis[:,0], medias_variaveis[:,1])  # eixo x e y
plt.title('Variável 1')
plt.xticks(medias_variaveis[:,0])           #indicar o nome dos genótipos

#Variável 2

plt.subplot(2,3,2)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,2])
plt.title('Variável 2')
plt.xticks(medias_variaveis[:,0])

##Variável 3

plt.subplot(2,3,3)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,3])
plt.title('Variável 3')
plt.xticks(medias_variaveis[:,0])

##Variável 4
plt.subplot(2,3,4)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,4])
plt.title('Variável 4')
plt.xticks(medias_variaveis[:,0])

#Variável 5

plt.subplot(2,3,5)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,5])
plt.title('Variável 5')
plt.xticks(medias_variaveis[:,0])

plt.show()
nome = 'medias_variáveis_barras'
fig.tight_layout                                         #Adequar tamanho imagem

print('------------------------------------------------------------------------------------------')
print(' ')

#Gráfico dispersão

print('Dispersão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.')
print(' ')

print('RESPOSTA')
print(' ')

print('Gráficos - Dispersão')
plt.style.use('ggplot') #tipo de gráfico
fig = plt.figure('Gráficos dispersão') # Título da figura
plt.subplot(2,2,1)                      # 1, 2 - delimitam como seria a figura    1 - posição do gráfico
plt.scatter(medias_variaveis[:,1], medias_variaveis[:,2], s=50, alpha=1, c='red')    #coordenada x- [:,1] coordenada y- [:,2] tamanho- s=50 transparencia- alpha=1

plt.title('Dispersão') #título do gráfico
plt.xlabel('Var 1') #título dos eixos x e y
plt.ylabel('Var 2')
plt.subplot(2,2,2)
plt.scatter(medias_variaveis[:,1], medias_variaveis[:,3], s=50, alpha=1, c='red')

plt.title('Dispersão')
plt.xlabel('Var 1')
plt.ylabel('Var 3')
plt.subplot(2,2,3)
plt.scatter(medias_variaveis[:,2], medias_variaveis[:,3], s=50, alpha=1, c='red')

plt.title('Dispersão')
plt.xlabel('Var 2')
plt.ylabel('Var 3')
fig.tight_layout()
plt.show()

print('------------------------------------------------------------------------------------------')
print(' ')
########################################################################################################################
########################################################################################################################