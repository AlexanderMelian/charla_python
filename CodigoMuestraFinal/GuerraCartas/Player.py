class Player():
    points = 0
    def __init__(self, username):
        self.username = username

    def updatePoints(self, points):
        self.points = points
    
    def resetPoints(self):
        self.points = 0

    def sumPoints(self, points):
        self.points += points

    def __str__(self):
        return "Username: {} \nPoints: {}".format(self.username, self.points)
