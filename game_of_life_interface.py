import game_of_life
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


print("Let the Game of life begin!")

# Next iteration using ndarray.view() to make changes to a view of the board
# Then assign back to game.board
game = game_of_life.Board((12,12)) # Start with seeded board
plt.ion()
img = plt.imshow(game.board)
for n in range(100):
	next_generation = game.board.copy()
	for index, cell in np.ndenumerate(game.board):
		count = game.get_live_neighbor_count(index)
		if cell == 0 and count == 3:
			next_generation[index] = 1 # Reproduction
		elif cell == 1 and  count < 2 or count > 3:
			next_generation[index] = 0 # Death from under/over population
		else:
			pass
	game.board = next_generation
	img.set_data(game.board)
	plt.draw()
	plt.pause(0.2)