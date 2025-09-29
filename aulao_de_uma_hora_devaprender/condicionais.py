# Condicionais if elif else
'''
E ae Erica, bora dar uma saida hoje?
Se eu terminar meu trabalho eu consigo.

'''
trabalho_terminado = False
if trabalho_terminado == True:
    print('Bora!')
else: 
    print('Não posso sair')


'''
Ei, Você consegue me ajudar a mover essas caixas lá para fora hoje a tarde?

Se eu estiver livre, sim. Mas se não der, pede meu irmão para te ajudar

'''

estou_livre = input('você esta livre sim ou não?')
if estou_livre == 'sim':
    print('ok, bora mover as caixas!')
else: 
    print('Pedi ajuda pro meu irmão')


# Como lidar com mais de 2 condições?
'''
Eu cheguei atrasado na aula. Ainda posso entrar?

se for a primeira ou segunda vez que vocÊ chega atrasado, pode sim. Mas se for a terceira vez, você será suspenso.

'''

atrasos = 2
if atrasos >= 3:
    print('Você esta suspenso')
elif atrasos == 2:
    print('Mais uma falta estara suspenso')
elif atrasos == 1:
    print('Mais duas faltas você estara suspenso')
else:
    print('Pode entrar')


# Problema:
# Crie um programa que receba dois valores e exibe quela é o maior entre eles.

'''
# Método 5Q's para montar um algoritimo:


analise criticamente o problema e descubra:
(Tente ewxplicar este problema para vc mesmo em voz alta e peça mais
informações/investigue mais ate que vc compreenda completamente o problema)

1. Quais são os dados de entrada necessários?
-O primeiro valor
- o segundo valor

2. O que devo fazer com esses dados?
- comparar os valores para saber qual o maior
3. Quais as restrições deste problema?
- Preciso ter os dois valores
4. Qual é o resultado esperado?
- Exibir o maior valor na tela
5. Qual é a sequencia de passos a ser feita para chegar ao resultado esperado(pseudocódigo)?
receber os numeros
- receber primeiro valor
- receber segundo valor
- comparar se o primeiro valor é maior que o segundo valor


'''
print('qual numero é o maior?')
numero_a = int(input('Digite o primeiro numero:'))
numero_b = int(input('Digite o segundo numero:'))

if numero_a > numero_b:
    print('Este numero é o maior:', numero_a)
else:
    print('Esse numero é o maior:', numero_b)