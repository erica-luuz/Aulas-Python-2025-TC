#%%

# uma maneira de definir listas
from numpy import mean


idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)


# %%

erica = ["erica", 43, True,  3, "casada", 4000]

print(erica)
# %%
type(erica)

#%%

#idade
print(erica[1])

#renda
print(erica[5])

#nome
print(erica[0])
# %%
idades = [28, 42, 43, 35, 39, 28, 38, 42, 55]

sum(idades)
print('soma das idades: ', sum(idades))

qtd_idades = len(idades)
media = sum(idades) / qtd_idades
print('media das idades: ', media)
# menor idade

print('menor idade: ', min(idades))

# maior idade
print('menor idade: ', max(idades))
# %%

erica = [
        "erica", 
         43, 
         True, 
         "casada",
         ["Felix", "Lolo", "Mel"],
         ["Nicollas", "Luccas", "Benjamim"]
         ]

len(erica)
erica[5]
erica[5][0]

#ou

filhos = erica[5]
primeiro_filho = filhos[0]
print(primeiro_filho)


# %%

tamanho = len(erica)
pos = tamanho - 1
erica [pos][0]

filhos = erica[pos]

erica[pos][len(filhos) - 1]

# %%
erica[-1]

# 37.22 minutos