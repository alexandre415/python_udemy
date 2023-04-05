nome = input('Digite o seu nome:')
idade = input('Digite a sua idade:')

if not (nome and idade):
    
    print('Desculpe, você deixou campos vazios ')

else:

    print(f'O seu nome é {nome}')
    print(f'O seu nome invertido é {nome[::-1]}')
    print(f'A primeira letra do seu nome é {nome[0]}')
   
    qtd_nome = len(nome)
  #  ultima_letra = nome[qtd_nome]
   # print(ultima_letra)

    if '' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome nao contém espaço')

    print(f'A última letra do seu nome é {nome[qtd_nome-1]}') #forma pior de se fazer
    #OU PODE SER
    print(f'A última letra do seu nome é {nome[-1]}') 

    print(f'Seu nome contém {qtd_nome} letras')
    #print(f'A ultima letra é {ultima_letra}')
