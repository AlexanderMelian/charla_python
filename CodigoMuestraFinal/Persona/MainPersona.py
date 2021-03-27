from Person import *

P1 = Person("Jorge", 20)
print(P1)
P2 = Person("Pamela", 30)
print(P2)

print("-------------")
P1.updateAge(21)
P2.updateAge(33)
print(P1)
print(P2)
print("--------------")
P1.updateName("Steven")
P2.updateName("Romina")
print(P1)
print(P2)
