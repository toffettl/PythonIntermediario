caminho_arquivo = "C:\\Users\\felip\\OneDrive\\Área de Trabalho\\PythonIntermediario\\ArquivosManipulados\\"
caminho_arquivo += "criado.txt"

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())
print('#' * 10)
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())