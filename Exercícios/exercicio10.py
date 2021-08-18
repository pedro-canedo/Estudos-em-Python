#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero >=0:
    print(f'O número {numero} digitado é um numero de valor positivo')
else:
    print(f'O número {numero} digitado é um numero de valor negativo')