from Player import *
from Deck import *

acum = 0
Pla1 = Player("Usuario1")
Pla2 = Player("Usuario2")
myDeck = Deck()

print(Pla1)
print(Pla2)
while myDeck.getLenCard() > 0:
    c1 = myDeck.getCard()
    c2 = myDeck.getCard()
    if (c1[1] == "comodin" and c2[1] == "comodin") or (c1[0] == c2[0]):
        acum += c1[0]*2
        continue
    if c1[0] > c2[0]:
        acum += c1[0] + c2[0]
        Pla1.sumPoints(acum)
    else:
        acum += c1[0] + c2[0]
        Pla2.sumPoints(acum)
    acum = 0

print("Juego terminado")
print(Pla1)
print(Pla2)
print("Resto: ", acum)