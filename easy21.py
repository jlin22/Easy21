from random import randint, random
from time import sleep

class Card:
	def __init__(self):
		self.value = randint(1, 10)

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
		return self.value if self.color == 'black' else -self.value

class Player:
	def __init__(self):
		self.cards = []
		self.stick = False

	def get_value(self):
		sum = 0
		for card in self.cards:
			sum += card.get_value()
		return sum

	def add_card(self, card):
		self.cards.append(card)

	def action(self, command):
		if command == 'stick':
			self.stick = True
		elif command == 'hit':
			self.cards.append(Card())
		else:
			pass

class Agent(Player):
	def __init__(self):
		super().__init__()

	def __repr__(self):
		# only display one card for the actual game
		return 'Agent:' + str(self.cards) + ' Value:' + str(self.get_value())

class Dealer(Player):
	def __init__(self):
		super().__init__()

	def __repr__(self):
		# only display one card for the actual game
		return 'Dealer:' + str(self.cards) + ' Value:' + str(self.get_value())

	def act(self):
		if self.get_value() < 17:
			self.action('stick')
		else:
			self.action('hit')

class Game:
	def __init__(self):
		self.dealer = Dealer()
		self.dealer.add_card(Card())
		self.dealer.cards[0].set_color('black')

		self.agent = Agent()
		self.agent.add_card(Card())
		self.agent.cards[0].set_color('black')

		# game only ends when dealer is done
		self.game_over = False

	def run(self):
		while (self.agent.stick == False):		
			print(self.dealer)
			print(self.agent)
			command = input('What will the agent do? ')
			self.agent.action(command)
			print()
			if (self.agent.get_value() > 21 or self.agent.get_value() < 1):
				print(self.dealer)
				print(self.agent)
				print()
				return -1 

		while (self.dealer.stick == False):
			sleep(1)
			print(self.dealer)
			print(self.agent)
			print()
			if self.dealer.get_value() < 17:
				command = 'hit'
			else:
				command = 'stick'
			self.dealer.action(command)
			print('Dealer ' + command)
			if (self.dealer.get_value() > 21 or self.dealer.get_value() < 1):
				print(self.dealer)
				print(self.agent)
				print()
				return 1 

		print(self.dealer)
		print(self.agent)
		print()
		if self.dealer.get_value() > self.agent.get_value():
			return -1
		elif self.dealer.get_value() == self.agent.get_value():
			return 0
		else:
			return 1


def main():
	game = Game()
	print('Reward:' + str(game.run()))

main()
