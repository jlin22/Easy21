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
		if color != 'black' or color != 'red':
			pass
		self.color = color
	def get_value(self):
		return 0

class Player:
	def __init__(self):
		self.cards = []
	def get_value(self):
		sum = 0
		for card in self.cards:
			sum += card.get_value()
		return sum
	def add_card(self, card):
		self.cards.append(card)
	def action(self, command):
		pass

class Agent(Player):
	def __init__(self):
		super()	

class Dealer(Player):
	def __init__(self):
		super()	
		
class Game:
	def __init__(self):
		self.dealer = Player()
		self.agent = Player()

def generate_card():
	return randint(0, 10)

def main():
	card = Card()
	print(card)

main()
