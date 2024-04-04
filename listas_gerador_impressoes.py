from sys import getsizeof

''' Generator Expressions: Uma forma mais rápida para listas, dicionários e etc,
    Menos memória alocada, 
    Valores em bytes.
    Serve para criar uma lista e gerar valores dentro dessa lista '''

numeros = [x * 10 for x in range(6)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

numeros = (x * 10 for x in range(6))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))