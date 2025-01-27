x = 1

def escopo():
    global x
    x = 10

    def outraFunc():
        global x
        x = 11
        y = 2
        print(x, y)

    outraFunc()
    print(x)

print(x)
escopo()
print(x)