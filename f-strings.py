"""
Formatação básica de strings

s - string
d - int
f - float
.<numero de dígitos>f
x ou X - Hexadecimal
(caracter)(><^)(quantidade)
> - Esquerda
< - Direita
^- Centro
Sinal - + ou -
Ex.: 0> - 100, .1f
conversion flags - !r - !s - !a  -> ler a respeito
padd é uma largura fixa que voce coloca na variavel
"""

nome = 'Dog'
print(f'{nome}')
print(f'{nome: >10}')# cria um espaça de 10 caracteres
print(f'{nome: <10}')# cria um espaça de 10 caracteres
print(f'{nome: ^10}.')# tenta colocar o nome no centro respeitando os 10 caracteres
print(f'{nome:$^10}')#coloca o nome no centro respeitando os 10 caracteres e acrescenta $ nos espaços 
# NAO PODE TER ESPAÇO ENTRE O : e o ^
print(f'{120938.12093182381:,.2f}')#coloca , . mas o python tem biblioteca q trata somente disso.
print(f'{nome}')

