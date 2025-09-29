
# Variáveis
velocidade_internet = 400
print(velocidade_internet)

# Números inteiros (int)
idade = 15
# Núemros decimais (float)
nota = 8.5
# Textos(strings) (str)
nome_completo = 'Erica Giselle'
# Booleanos (True ou False) (bool)
pode_entrar = True

print(idade, nota, nome_completo, pode_entrar)

# para saber qual é o tipo que esta dentro da minha variável
print(type(pode_entrar))

# Escreva 1 problema - Valor por hora
# Escreva um programa que retorna o valor hora de um funcionário
# com base no seu salário mensal e horas trabalhadas por mês.

'''
# Método 5Q's para montar um algoritimo:


analise criticamente o problema e descubra:
(Tente ewxplicar este problema para vc mesmo em voz alta e peça mais
informações/investigue mais ate que vc compreenda completamente o problema)

1. Quais são os dados de entrada necessários?
- Sala´rio Mensal
- Quantidade de horas trabalhadas

2. O que devo fazer com esses dados?
- Clacular o valor hora

3. Quais as restrições deste problema?
- Precisa ter um valor do salário mensal
- Precisa ter um valor da quantidade de horas trabalhadas

4. Qual é o resultado esperado?
- Exibir o valor hora da pessoa, com base no cálculo de valor hora

5. Qual é a sequencia de passos a ser feita para chegar ao resultado esperado(pseudocódigo)?
receber salário mensal
receber quantidade de horas
'''
salario_mensal = input('Qual é o seu salario mensal:')
quantidade_horas_trabalhadas = input('Quantas horas vc trabalha por mês:')
valor_hora = float(salario_mensal) / int(quantidade_horas_trabalhadas)
print('Este funcionário recebe por hora: ', valor_hora)




