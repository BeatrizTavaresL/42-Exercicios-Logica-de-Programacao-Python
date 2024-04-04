rendimento = int(input('Qual o rendimento da tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

def calculo_tinta():
    area = largura * altura
    total_tinta = area / rendimento
    print('Você precisa de', total_tinta,'de latas de tinta!')
calculo_tinta()