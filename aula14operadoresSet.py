s1 = {1, 2, 3, 3, 2, 1}
s2 = {1, 2, 3, 3, 2, 1}
s3 = s1 | s2 #| vai unir os sets
print(s3)
s3 = s1 & s2 #Vai mostrar oq contém nos dois
print(s3)
s3 = s1 - s2 #Vai mostrar o item que só existe no s1
print(s3)
s3 = s1 ^ s2 #Retorna os itens unicos em ambos
print(s3)