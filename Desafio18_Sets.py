
# Sets evita items duplicados. 
friends1 = {'João', 'Jéssica', 'Paulo', 'Tereza'}
friends2 = {'Brenda', 'Paulo', 'Tereza', 'Bianca'}

amigos_comum = friends1.intersection(friends2)
print(amigos_comum)

amigos_comum = friends1.union(friends2)
print(amigos_comum)

