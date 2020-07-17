##### Pacote utilizado #####

# Instalação
import numpy as np

########################################################################################################################
#####################################################################################################################

##### EXERCÍCIO 03 #####'

print('Exercício 3')
print(' ')

# Questão A

print('a- Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor'
      ' qualquer, baseada em um loop (for). ')
print(' ')

"""A utilidade de fazer uma função em um arquivo externo é voce poder utilizar ela em diferentes momentos, quando você 
está fazendo scripts diferentes. E quando for usar, basta chamar a função para dentro de seu script.
Para criar uma função, vou usar o comando def + nome da função+ argumento ( o que ela vai precisar pra ser executada), que
no caso é um vetor qualquer.
Além disso, vou criar a função com for, ou seja, para ser aplicada repetidamente a cada elemento do vetor, por vez, em um 
loop continuo.
No primeiro caso, deterinei o somador e o it = 0, o que vai ser somado a cada etapa e as etapas. É importante que as etapas
 da função for, sejam identadas. Declara o somador e o it a cada passo, recebendo o próximo elemento e 1, respectivamente.
 E cria a função, e o comando para retornar o resultado."""

print('RESPOSTA')
print(' ')

def media (vetor):
    somador = 0
    it = 0
    for el in vetor:
        somador += el  # somador = somador + i
        it+=1  # it = it+1
    mean = somador/it
    return mean

def variancia_amostral (vetor):
    somador = 0
    it = 0
    sdq = 0
    for el in vetor:
        somador += el  # soma = soma + i
        it += 1  # it = it+1
        sdq += el**2 #sdq = sdq + i**2
    var = (sdq - ((somador**2/it)))/(it-1)
    return var

