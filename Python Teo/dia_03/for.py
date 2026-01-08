#%%
nome = 'Erica Giselle'

for letra in nome:
    print (letra)
# for percorre os elementos de um objeto.
# %%
nome =  'erica Giselle'

for i in nome:
    print(i)

#%%

numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero * i )
# %%

# Quais numeros são divisiveis por 4
# No intervalo [4-100]

for i in range(4, 101):
    if i % 4 == 0:
        print(i)
# %%
