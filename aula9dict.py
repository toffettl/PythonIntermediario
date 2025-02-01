pessoa = {
    "nome" : "Felipe",
    "sobrenome" : "Toffetti",
    "idade" : 16,
    "altura" : 1.77,
    "enderecos" : [
        {"rua" : "av.coisa", "numero" : 123},
        {"rua" : "av.outra", "numero" : 456}
    ]
}
print(pessoa["nome"])
print(pessoa["enderecos"])

for chave in pessoa: # para percorrer as chaves do dict
    print(chave, pessoa[chave])