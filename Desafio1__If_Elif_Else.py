# Desafio com If, Elif, Else 

''' 
   Criar um programa que dependendo da temperatura (em celcius) do steak ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

   Temperatura - Cozimento
   120F ou 48C - Rare (Selada)
   130F ou 54C - Medium rare (Ao ponto para o mal)
   140F ou 60C - Medium (Ao ponto)
   150F ou 65C - Medium well (Ao ponto para o bem)
   160F ou 71C - Well done (Bem passada)

'''

temperatura = int(input('Qual a temperatura da carne: '))

# rare = 48 
# medium_rare = 54 
# medium = 60
# medium_well = 65
# well_done = 71


# if temperatura < rare: 
#     print('Selada')
# elif temperatura <= medium_rare: 
#     print('Ao ponto para o mal')
# elif temperatura <= medium: 
#     print('Ao ponto')
# elif temperatura <= medium_well: 
#     print('Ao ponto para o bem')
# else:
#     print('Bem passada')


if temperatura < 48: 
    print('Cozinhar por mais uns minutos: ')
elif temperatura in range(48,53): 
    print('Selada!')
elif temperatura in range(54,59): 
    print('Ao ponto para o mal!')
elif temperatura in range(60,64): 
    print('Ao ponto!')
elif temperatura in range(65,70): 
    print('Ao ponto para o bem!')
elif temperatura in range(71,75):
    print('Bem passada!')
elif temperatura in range(80,85):
    print('Passou do ponto!')
elif temperatura > 85: 
    print('Carne queimada!')






            





