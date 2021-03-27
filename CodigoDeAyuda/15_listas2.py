lista = ["hola", 24, 30.2, "chau"]
print(lista)

lista.append("nuevo valor")
print(lista)#['hola', 24, 30.2, 'chau', 'nuevo valor']

lista.extend(["Otra", "lista", 12])
print(lista)#['hola', 24, 30.2, 'chau', 'nuevo valor', 'Otra', 'lista', 12]

lista.insert(2, "nuevo valor")
print(lista)#['hola', 24, 'nuevo valor', 30.2, 'chau', 'nuevo valor', 'Otra', 'lista', 12]


print(lista.pop(),lista)# 12 ['hola', 24, 'nuevo valor', 30.2, 'chau', 'nuevo valor', 'Otra', 'lista']

print(lista.pop(1),lista)# 24 ['hola', 'nuevo valor', 30.2, 'chau', 'nuevo valor', 'Otra', 'lista']