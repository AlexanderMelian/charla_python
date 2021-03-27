dict1 = { "clave1": "valor1",3:[7.8, "algo"], "clave1": "claverepe"}
print(dict1)# {'clave1': 'claverepe', 3: [7.8, 'algo']}

dict2 = dict(clave1="valor", clave2=2, clave3 = 7.8)
print(dict2)#{'clave1': 'valor', 'clave2': 2, 'clave3': 7.8}


print(len(dict1)) # 2

print(dict1["clave1"]) # claverepe

print(dict1.get(3)) # [7.8, 'algo']

print(dict1[3][0]) # 7.8


dict1["clave3"] = "nuevo"

dict1.pop("clave3")

print(dict1)# {'clave1': 'claverepe', 3: [7.8, 'algo']}