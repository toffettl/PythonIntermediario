lista = [numero for numero in range(10)] 
lista2 = [numero * 2 for numero in range(10)] 

print(lista)
print(lista2)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novosProdutos = [
    {**produto, "preco": produto["preco"] * 1.05} 
    if produto["preco"] > 20 else {**produto}
    for produto in produtos
]
print(*novosProdutos, sep="\n") #sep é o separador

lista3 = [n for n in range(10) if n < 5] #filtro
print(lista3)
