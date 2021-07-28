#o programa pede para que o usuário informe a data de nascimento em seguida ele retorna se o usuário  tem ou não o voto obrigatório
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO. '


nasc = int(input('Em que ano você nasceu ? '))
print(voto(nasc))