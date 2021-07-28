#o programa cadastra várias pessoas quantas você desejar e lista quantas foram cadastradas, a media de idade das pessoas, quais mulheres foram cadastradas e quem está acima da média em idade
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str (input ('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MFN':
            break
        print('ERRO ! por favor, digite apenas M, F ou N. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO ! responda apenas [S/N] ')
    if resp == 'N':
        break
print('=-' * 30)
print(f'Ao todo temos: {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade']>= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
            print()
print('<< ENCERRADO >>')