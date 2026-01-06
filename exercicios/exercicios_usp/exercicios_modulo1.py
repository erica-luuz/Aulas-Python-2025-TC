# Faça uma calculadora simples, usando Soma, Subtração, Multiplicação, Divisão
# Potenciação
#%%
print("Minha Calculadora")
operacao = input('Digite qual operação você quer usar: Soma, Subtração, Divissão, Potênciação')
valor1 = input('Digite o primeiro valor a ser calculado:')
valor2 = input('Digite o segundo valor a ser calculado')

if operacao == 'Soma':
    resultado = int(valor1) + int(valor2)
    print('O resultado da Soma é: ',resultado)
elif operacao == 'Subtração':
    resultado = int(valor1) - int(valor2)
    print('O resultado da Subtração é: ',resultado)
elif operacao == 'Multiplicação':
    resultado = int(valor1) * int(valor2)
    print('O resultado da Multiplicação é: ',resultado)
elif operacao == 'Divisão':
    resultado = int(valor1) / int(valor2)
    print('O resultado da Divisão é: ',resultado)
elif operacao == 'Potenciação':
    resultado = int(valor1) ** int(valor2)
    print('O resultado da Potenciação é: ',resultado)
else:
    print('Valor inválido')
# %%
