import game_of_life
import numpy as np

# What are the steps in the game?
# User initiates random seeding of first generation.
# Board is printed (allow with generation number)
# All cells in first generation are evaluated.
# Then repeat
# Game ends if all cells are dead for after evaluation.

print("Let the Game of life begin!")

# Next iteration using ndarray.view() to make changes to a view of the board
# Then assign back to game.board
game = game_of_life.Board((3,3)) # Start with seeded board
print(game.board)
next_generation = game.board.copy()
for index, cell in np.ndenumerate(game.board):
	count = game.get_live_neighbor_count(index)
	#print(index, "First generation:",cell, "Count:",count)
	if cell == 0 and count == 3:
		#print("live")
		new_value = 1 # Reproduction
		next_generation[index] = 1 # Reproduction
		#print(game.board == next_generation)
		#print("Second generation:",new_value)
	elif cell == 1 and  count < 2 or count > 3:
		#print("die")
		new_value = 0 # Death from under/over population
		next_generation[index] = 0 # Death from under/over population
		#print("Second generation:",new_value)
	else:
		pass
#print(game.board is next_generation)
#print(game.board == next_generation)
print(game.board)
print(next_generation)
game.board = next_generation
print(game.board)
