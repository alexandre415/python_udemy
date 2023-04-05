"""
fatiamento de string
012345678
olá mundo
-987654321
fatiamento [i:f:p] [::]
obs.: a funcao len retorna a qtd de caracteres da str
sempre quisermos o indice final, temos que pegar um numero a mais.
"""
bem_vindo = 'Buenas Noches!'

print(bem_vindo[4:8])#começa no indice 0
print(bem_vindo[0:8])#começa no indice 0
print(bem_vindo[:8])#começa no indice 0
print(bem_vindo[-8:-3])#começa no indice -14

#FUNÇÃO len CONTA OS CARACTERES DA String. contar é diferente de indice.

print(len(bem_vindo))

#fatiamento [i:f:p]
print(bem_vindo[0:9:2])# o p é de passo. de quanto em quanto voce quer q ele pule.

print(bem_vindo[::-1]) #ele inverte a string
