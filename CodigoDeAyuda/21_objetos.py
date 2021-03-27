class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person({}, {})".format(self.name, self.age)

    def __str__(self):
        return "Nombre: {}\nEdad: {}".format(self.name, self.age)

    def cumpleanios(self):
        self.age += 1



me = Person("Pepe", 22)


print(me)#Nombre: Pepe
# Edad: 22

print(repr(me))#Person(Pepe, 22)

me.cumpleanios()
print(me)# Nombre: Pepe
# Edad: 23