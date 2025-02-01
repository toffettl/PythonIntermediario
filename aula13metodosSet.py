s1 = set()
s1.add("Toffetti")
s1.add(1)
s1.update(("Olá mundo!")) #() pra não separar o iteravel
print(s1)
s1.discard("Toffetti")
