pessoa = {
    "nome" : "Felipe",
    "sobrenome" : "Toffetti"
}
print(len(pessoa)) #len() da o número de chaves
print(list(pessoa.keys())) #keys() retorna as chaves
print(list(pessoa.values())) #values() retorna os valores
pessoa.setdefault("idade", 0) #definir valor padrao para quando não existe
teste = pessoa.copy() #copia rasa
print(teste)
pessoa.pop("nome") #apaga o item
pessoa.popitem() #apaga o ultima adicionado 
pessoa.update({
    "nome" : "Sofia",
    "idade" : 18,
})