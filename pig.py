import random

class Game:
    pass

class Turn:
    pass

class Player:
    def __init__ (self, name):
        self.name = name

class Die:
    def __init__ (self, sides=6):
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)

player1 = Player("Human")
player2 = Player("Computer")

# while keep_rolling = True
# 	player_choice = input("Enter nothing to roll; enter anything to hold"))
# 	if player_choice = ""
# 		turn_score = 0
# 		turn_score += die.roll()
# 	else player_choice != ""
# 		#append turn_score to total_score#
# 		keep_rolling = False