import random

class Game:
    pass

class Turn:
    pass

class Player:
    def __init__ (self, name):
        self.name = name

class Dice:
    def __init__ (self, sides=6):
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)

player1 = Player("Human")
player2 = Player("Computer")