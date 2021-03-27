dict1 = {'clave1': 'claverepe', 3: [7.8, 'algo']}

items = dict1.items()
print(items) # dict_items([('clave1', 'claverepe'), (3, [7.8, 'algo'])])

keys = dict1.keys()
print(keys) # dict_keys(['clave1', 3])

values = dict1.values()
print(values) # dict_values(['claverepe', [7.8, 'algo']])


print(values) # dict_values(['claverepe', [7.8, 'algo']])
dict1["clave1"] = "nuevo"
print(values) # dict_values(['nuevo', [7.8, 'algo']])