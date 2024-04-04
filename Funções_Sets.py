''' Sets (Listas)   
    Similiar a listas, evita itens duplicados, não utiliza index. ''' 

s1 = {1, 2, 3, 4, 5, 6}
s1.update([6, 7, 8, 9, 10]) #junta as duaslistas, ficando '1,2,3,4,5,6,7,8,9,10'
s1.remove(10) # Gera um erro, caso o item desejado não esteja no set.
s1.discard(9) # Não gera um erro.
print(s1)