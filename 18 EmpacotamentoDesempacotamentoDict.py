a, b = 1, 2
a, b = b, a

pessoa = {
    "nome" : "Felioe",
    "Sobrenome" : "Toffetti",
}

dadosPessoas = {
    "idade" : 16,
    "Altura" : 1.6,
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

pessoaCompleta = {**pessoa, **dadosPessoas}
print(pessoaCompleta)

def mostroNomeados(*args, **kwargs):
    print("Não nomeados: ", args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostroNomeados(**pessoaCompleta)