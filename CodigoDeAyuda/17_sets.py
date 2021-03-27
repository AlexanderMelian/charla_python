set1 = set(["Hola", 24, 30.2, "Hola"])
print(set1) #{24, 30.2, 'Hola'}


set2 = {24, 30.2, "Hola", "Chau"}


print(len(set1)) # 3

set1.add("Algo")
print(set1)#{24, 'Hola', 'Algo', 30.2}
set1.discard("Algo")
print(set1)#{24, 'Hola', 30.2}

print(set1.union(set2)) # == set1 | set2
# {24, 'Hola', 'Chau', 30.2}

print(set1.intersection(set2)) # == set1 & set2
# {24, 30.2, 'Hola'}
print(set2.difference(set1)) # == set1 - set2
#{'Chau'}