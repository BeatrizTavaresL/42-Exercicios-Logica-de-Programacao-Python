# try: 
#     valor = int(input('Digite o valor do seu produto: '))
#     print(valor)
# except ValueError:
#     print('Favor digitar um número inteiro')
# else: 
#     print('Usuario digitou um valor correto')
#     resultado = valor * 2
#     print(resultado)

try: 
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um número inteiro')
finally:
    print('Código OK')
  