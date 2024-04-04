estoque = ['BMW X6', 'BMW i5', 'BMW i8']

pesquisa_carro = input('Digite o nome do carro que deseja comprar: ')

if pesquisa_carro in estoque:
    print('Este carro está disponível!')
else: 
    print('Este carro não está disponível!')

