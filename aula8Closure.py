def criarSaudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

bomDia = criarSaudacao("Bom dia")
boaNoite = criarSaudacao("Boa noite")

print(bomDia("Felipe"))
print(boaNoite("Sofia"))