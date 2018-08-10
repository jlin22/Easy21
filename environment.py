from random import randint, random
from card import Card

# state = (dealer, player_sum), action = hit or stick
def step(state, action):
	(dealer, player_sum) = state
	if state == 'terminal':
		pass
	elif action == 'stick':
		while dealer < 17 and dealer > 0:
			dealer += Card().true_value()	
		print(dealer)
		print(player_sum)
		if dealer > 21 or dealer < 1:
			return ['terminal', 1]
		elif dealer > player_sum:
			return ['terminal', -1]
		elif dealer == player_sum:
			return ['terminal', 0] 
		else:
			return ['terminal', 1]
		# terminal, play out dealer
	else:
		player_sum += Card().true_value()
		if player_sum > 21 or player_sum < 1:
			next_state = 'terminal'
		reward = -1 
		return [next_state, reward]

print(step((1, 21), 'stick'))