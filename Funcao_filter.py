valores = [20, 25, 30, 35, 40, 45,50]

# def remover_num(x):
#     return x > 30
# print(list(filter(remover_num, valores)))
print(list(filter(lambda x: x > 30, valores)))