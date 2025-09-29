'''
Faça um programa que vende uma garrfa de água:
a. Se o cliente escolher água mineral naturtal, sera cobrado R$ 1,50
b. Se o cliente escolher água mineral com gás, será cobrado R$ 2,50

'''
# %%
print('ESCOLHA SUA ÁGUA MINERAL')
agua = input('Escolha sua agua mineral: natural ou com gás: ')

natural = 'R$ 1,50'
com_gas = 'R$ 2,50'

if agua == 'natural':
    print('Agua mineral natural custa: ', natural)

elif agua == 'com gás':
    print('Agua mineral com gás custa: ', com_gas)

else:
    print('Valor invalido, digite novamente!!!!')

## outra fortma de fazer

texto = '''Escolha a sua água para comprar
(1) Água Mineral Natural
(2) Água Mineral com Gás
'''

opcao = input(texto)

natural = 'R$ 1,50'
com_gas = 'R$ 2,50'
mensagem = 'Sua conta deu: '

if opcao == '1':
    print(mensagem, natural)

elif opcao == '2':
    print(mensagem, com_gas)

else:
    print('Valor invalido, digite novamente!!!!')

