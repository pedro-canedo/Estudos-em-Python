# O objetivo é criar um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

class tintas:
    def __init__(self):
        self.lata = int(18)
        self.valor = float(80)
        self.rendimento = int(3) # metros para cada 1 litro de tinta

    pass
tinta = tintas()

area = int(input('Qual o tamanho em m² deseja pintar ?: '))
numeroLatasTinta = area / tinta.rendimento / tinta.lata
custoPintua = numeroLatasTinta * tinta.valor

print(f'A quantidade de latas de tintas a serem gastas é de {numeroLatasTinta:.2f} e o custo para esta pintura é de {custoPintua:.2f}')

