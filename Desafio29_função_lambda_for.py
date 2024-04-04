numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = lambda numero: numero ** 2 

resultados = []
for numero in numeros: 
    resultados.append(quadrado(numero))

print(f'Os quadrados dos números {numeros} são {resultados}')
