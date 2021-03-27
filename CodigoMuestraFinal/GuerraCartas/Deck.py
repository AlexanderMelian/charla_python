import random

class Deck():
    deck = []
    def __init__(self):
        number = [1,2,3,4,5,6,7,8,9,10,11,12]
        tipe = ["espada", "copa", "oro", "palo"]
        special = "comodin"
        self.deck.append([20,special])
        self.deck.append([20,special])
        for i in number:
            for j in tipe:
                card = [i,j]
                self.deck.append(card)
    
    def getDeck(self):
        return self.deck

    def getLenCard(self):
        return len(self.deck)

    def __str__(self):
        return "Deck:\n{}".format(self.deck)

    def getCard(self):
        maximum = len(self.deck)-1
        index = random.randint(0,maximum)
        card = self.deck[index]
        self.deck.pop(index)
        return card
