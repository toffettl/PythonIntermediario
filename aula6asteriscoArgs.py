x, y, *resto = 1, 2, 3, 4 #Colocar * recebe oq sobrou depois de x e y
print(x, y, resto)

def soma(x, y):
    return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

somas = soma(1, 2, 3, 4, 5)
print(somas)
