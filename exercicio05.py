#recebe os valores e retorna eles alocados em uma lista
numeros = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, tente novamente...')
    r =  str(input('Quer continuar ? [S/N]: '))
    if r in 'Nn':
        break

print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros} ')