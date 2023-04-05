entrada = input('[E]ntrar ou [Sair]')
senha_digitada= input('Digite sua senha: ')
senha_autorizada = 'xandao'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_autorizada:
    print('Seja bem vindo ao sistema')

else:
    print('Sair')

    #SAO CONSIDERADOS FALSY -> 0, 0.0, '', False
#and
print(True and True and True)
print(True and False and True)
print(True and 0 and True)# retorna o valor falso e nao checa o resto
    #existe o tipo None que é utilizado para não valor

#OR
print(True or False)

#NOT 
# not true = false
#not false = true
#usado para inverter expressoes

senha = input('Senha:')

if not senha:

    print('Voce não digitou uma senha!')


#OPERADORES IN(ESTÁ ENTRE) E NOT IN( NÃO ESTÁ ENTRE)
# Strings são iteráveis
#0 1 2 3 4 5 
#x a n d a o
#-5 -4 -3 -2 -1

nome = 'xandao'

print(nome[2])

print(nome[-4])
print(10 * '-')
print('a' in nome)
print('a' not in nome)

nome = input('Digite o seu nome: ')
letra = input('Digite a letra que deseja achar: ')

if letra in nome:
    print(f' A letra {letra} esta dentro do nome {nome}')

else:
    print(f'A letra {letra} não está dentro do nome {nome}')


