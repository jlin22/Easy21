from random import randint, random

class Card:
	def __init__(self):
		self.value = randint(1, 10)

		if random() < 1 / 3: 
			self.color = 'red'
		else:
			self.color = 'black'

	def true_value(self):
		if self.color == 'red':
			return - self.value
		else:
			return self.value
