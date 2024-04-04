aluno = {'nome': 'Ana', 'idade': 30, 'aprovação': 'true'}
aluno['nome'] = 'Beatriz' # Serve para substituir algo. 
aluno.update({'nome':'José', 'idade': 16}) # atualizar mais de um item.
# print(aluno.get('endereço', 'Não existe')) # para buscar um item.
# del aluno['idade'] # para remover um item.
# print(aluno) 
#print(aluno['idade']) # serve para buscar uma informação pela chave. 

for x in aluno.values(): # para mostrar os valores ... for x in aluno.keys() para mostrar apenas as chaves.
    print(x)


for keys, values in aluno.items(): # para mostrar as chaves e os valores.
    print(keys, values)
    

