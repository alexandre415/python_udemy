nome = input('Qual o seu nome?')
print(f'O seu nome é : {nome}')

numero_1 = input('Digite um número:')
numero_2 = input('Digite outro número:')

print('A soma dos números é: ', numero_1 + numero_2) # AQUI ELE CONCATENA O NUMERO PQ TUDO É STR

numero_3 = int(input('Digite um número:'))
numero_4 = int(input('Digite outro número:')) #FUNCIONA FAZENDO CAST MAS DA PAU CASO DIGITE ALGO DIFERENTE
#NAO É ACONSELHADO UTILIZAR DESSA FORMA

print('A soma dos números é: ', numero_3 + numero_4)