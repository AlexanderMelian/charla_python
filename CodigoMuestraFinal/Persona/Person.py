class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def updateName(self, name):
        self.name = name

    def updateAge(self, age):
        self.age = age

    def __str__(self):
        return "NAME: {}\tAGE: {}".format(self.name, self.age)
