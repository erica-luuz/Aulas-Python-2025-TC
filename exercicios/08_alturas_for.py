"""Faça um programa que conte receba 4 alturas usando
um alço de repetição e realize a soma dessas altura.
"""
#%%
soma = 0    # Valor final
qtde_entradas = 4     # o contador de entradas

for i in range(qtde_entradas):
    altura = input('Entre com a altura: ')
    altura = float(altura)
    soma += altura
   
print('Soma das alturas:', soma)
