# set [listas]


list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1)
print(num2)
print(num1 | num2) # Union ... Vai unir as duas listas, tirando os itens repetidos e remove os duplicados.
print(num1 - num2) # Difference ... Não mostra os números que tem na list 2.
print(num1 ^ num2) # Symmetric Difference ... Retira todos os duplicados das duas listas.
print(num1 & num2) # And ... Mostra apenas os números duplicados
print(len(num1)) # Para contar quantos itens tem na list2. 