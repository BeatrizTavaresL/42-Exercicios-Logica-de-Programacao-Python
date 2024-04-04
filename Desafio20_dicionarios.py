# Dicionário sempre retorna o valor da chave. 


capitais = {'Brasil': 'Brasilia',
                    'Argentina': 'Buenos Aires',
                    'Chile': 'Santiago',
                    'Australia': 'Canberra',
                    'Canada': 'Ottawa'}

pais_usuario = input('Digite o nome do pais: ')

if pais_usuario in capitais: 
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')
else:
    print('Desculpa, não temos informações sobre a capital desse pais!')