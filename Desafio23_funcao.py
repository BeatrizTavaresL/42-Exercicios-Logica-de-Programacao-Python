def potencia(base, expoente=2):
    return base ** expoente
numero = int(input('Digite o número base: '))
expoente = (input('Digite um expoente (default 2): '))

if expoente: 
    print(f'O resultado é: {potencia(numero,int(expoente))}')

else:
    print(f'O resultado é: {potencia(numero)}')