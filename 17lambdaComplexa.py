def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criaMultiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = criaMultiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(
    executa(
        lambda x, y: x + y , #isso é a mes
        2, 3
    ),
    executa(soma, 2, 3)
)