#Faça uma programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.
numero = input("Digite um numero inteiro para calcular a raiz quadrada:")
numero = int(numero)

raiz_quadrada = numero **(1/2)   # numero ** 0.5
raiz_quadrada= round(raiz_quadrada,4) # para arredondar para 4 digitos

print("Raiz quadrada de", numero, "é:", raiz_quadrada)