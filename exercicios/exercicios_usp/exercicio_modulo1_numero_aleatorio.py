#Implemente um código que seleciona um número aleatório de 1 a 10 e você tem que adivinhar qual é.
#Dica: use a função rand ou uma parecida para gerar esse número aleatório
#%%

import random

print("=== JOGO DA ADIVINHAÇÃO ===")

# Computador escolhe um número secreto
numero_secreto = random.randint(1, 10)

# Usuário tenta adivinhar
palpite = int(input('Adivinhe o número de 1 a 10: '))

# Verifica se acertou
if palpite == numero_secreto:
    print('Parabéns! Você acertou!')
else:
    print('Errou! O número era:', numero_secreto)

