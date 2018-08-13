from random import randint, random
from card import Card
import numpy as np

# state = (dealer, player_sum), action = hit or stick
def step(state, action):
	(dealer, player_sum) = state
	if state == 'terminal':
		pass
	elif action == 'stick':
		while dealer < 17 and dealer > 0:
			dealer += Card().true_value()	
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
		else:
			next_state = (dealer, player_sum)
		reward = -1 
		return [next_state, reward]

def montecarlo(N_zero, N_state, N_state_action, value, num_iters = 1000):
	# 0 = stick, 1 = hit
	for i in range(num_iters): # run an episode

		# initialize the game
		dealer = Card().value 
		player_sum = Card().value
		state = (dealer, player_sum)

		states_visited = [] 
		# epsilon greedy policy
		epsilon = N_zero / (N_zero + N_state[dealer - 1, player_sum - 1])
		while state != 'terminal':
			if random() < epsilon: # epsilon
				if random() < 1 / 2:
					state, reward = step(state, 'stick')
					states_visited.append((dealer, player_sum, 0))
				else:
					state, reward = step(state, 'hit')	
					states_visited.append((dealer, player_sum, 1))
			else: # greedy policy
				if value[dealer - 1][player_sum - 1][0] > value[dealer - 1][player_sum - 1]:
					# means return for stick > return for hit
					state, reward = step(state, 'stick')
					states_visited.append((dealer, player_sum, 0))
				else:
					state, reward = step(state, 'hit')
					states_visited.append((dealer, player_sum, 1))

		# here state = 'terminal', and reward = -1, 0, 1
		for s in states_visited:
			dealer, player_sum, action = s		
			value[dealer - 1][player_sum - 1][action] += reward

N_zero = 100
N_state = np.zeros((10, 21)) 
N_state_action = np.zeros((10, 21, 2))
value = np.zeros((10, 21, 2))
montecarlo(N_zero, N_state, N_state_action, Q, num_iters = 1)
#print(Q)
