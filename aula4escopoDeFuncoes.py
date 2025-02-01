x = 1 # ESSE AQUI

def escopo():
    x
    x = 10

    def outraFunc():
        global x #global para se referir ao primeiro x
        x = 11
        y = 2
        print(x, y)

    outraFunc()
    print(x)

print(x)
escopo()
print(x)
