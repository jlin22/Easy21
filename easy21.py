from random import randint, random

class Card:
	def __init__(self):
		self.value = randint(0, 10)
		if random() < 1/3:
			self.color = 'red'
		else:
			self.color = 'black'
	def __repr__(self):
		return 'Card<value:' + str(self.value) + ', color:' + self.color + '>'
	def set_color(self, color):
		self.color = color

class Player:
	def __init__(self):
		pass	

class Game:
	def __init__(self):
		self.dealer = Player()
		self.agent = Player()

def generate_card():
	return randint(0, 10)

def main():
	game_over = False
	while not game_over:
		input()

main()