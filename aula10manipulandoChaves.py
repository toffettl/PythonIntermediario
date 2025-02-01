pessoa = {}

pessoa["nome"] = "Felipe" #criando chave

chave = "sobrenome"
pessoa[chave] = "Toffetti"
pessoa["teste"] = "teste"

print(pessoa[chave])
print(pessoa["nome"])

del pessoa["teste"] #para deletar a chave "teste"

if pessoa.get("teste") is None: #.get quando não existe retorna None
    print("Não existe!")
else:
    print("Existe!")

