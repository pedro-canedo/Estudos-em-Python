print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar ? R$: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'total de {totced} cédulas de R$:{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break