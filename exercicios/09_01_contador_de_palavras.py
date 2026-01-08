# Contar quantas vezes a letra "a" aparece em uma palavra
palavra = input("Digite uma palavra: ")
contador = 0
indice = 0

while indice < len(palavra):
    if palavra[indice] == 'a':
        contador += 1
    indice += 1

print(f"A letra 'a' aparece {contador} vez(es) na palavra '{palavra}'.")
               