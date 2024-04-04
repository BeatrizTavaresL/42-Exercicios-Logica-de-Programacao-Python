def fatorial(numero: int):
    if numero == 0 or numero == 1:
        return 1 
    else: 
        return numero * fatorial(numero - 1)
nu = int(input('Digite um número: '))
print(f'O fatorial de {nu} é {fatorial(nu)}')