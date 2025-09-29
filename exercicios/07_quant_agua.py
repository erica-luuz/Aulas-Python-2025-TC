

texto = '''Escolha a sua água para comprar
(1) Água Mineral Natural - R$ 1.50
(2) Água Mineral com Gás - R$ 2.50
'''

opcao= input(texto)

valor_item = 0

if opcao == '1':
    valor_item = 1.5
elif opcao == '2':
    valor_item = 2.5
else:
    print('Entre com a opção correta')

qtde = input('Quantas garrafas? ')
qtde = int(qtde)

valor_total = valor_item * qtde

print('Sua conta deu: R$ ', valor_total)