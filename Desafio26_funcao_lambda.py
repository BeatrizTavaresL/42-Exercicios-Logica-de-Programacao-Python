# def cubo(numero): 
#     return numero ** 3

cubo = lambda numero: numero ** 3 
user_number = int(input('Digite um número: '))
print(f'O cubo de {user_number} é {cubo(user_number)}')