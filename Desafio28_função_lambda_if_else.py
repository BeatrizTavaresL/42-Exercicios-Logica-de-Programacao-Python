par_ou_impar = lambda numero: 'Par' if numero % 2 == 0 else 'Impar'
usuario = int(input('Dígite um número: '))
print(f'O número {usuario} é {par_ou_impar(usuario)}')