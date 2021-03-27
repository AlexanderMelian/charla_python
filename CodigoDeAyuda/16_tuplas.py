tupla = ("Hola", 24, 30.2, "Chau")


print(len(tupla)) # 4

print(tupla.index(24)) # 1

print(tupla[2]) # 30.2

print(tupla[1:]) # (24, 30.2, 'Chau')

tupla2 = ("Nueva", "Tupla")

tupla3 = tupla + tupla2

print(tupla3) # ('Hola', 24, 30.2, 'Chau', 'Nueva', 'Tupla')