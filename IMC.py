nome = 'Alexandre Cardoso'
altura = 1.66
peso = 65
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)

#formatação de string 'f-strings'

linha_1 = f'{nome} tem de {altura:.2f} altura e seu imc é {imc:.2f}' #RECONHECE A VARIAVEL ENTRE CHAVES, SEM COLOCANDO O 'F' ANTES DA STRING.

print(linha_1)