import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d


size = 1000
generations = 100
board = np.random.randint(2, size=(size,size))
plt.ion() # set matplotlib to interactive mode
img = plt.imshow(board)

def eval_cells(cell, count):
    """Evaluate and update a cell according to Conway's GOL rules."""
    if cell == 0 and count == 3:
        cell = 1 # Reproduction
    elif cell == 1 and  count < 2 or count > 3:
        cell = 0 # Death from under/over population
    else:
        pass
    return cell

veval_cells = np.vectorize(eval_cells)

for i in range(generations):
    previous_gen = board.copy()
    # Produce a board where each cell is filled with live neigbor count
    live_neighbor_counts = (convolve2d(previous_gen, np.ones((3,3)), mode="same") - previous_gen)
    # Evaluate each cell against Conway's COL rules to produce net generation
    next_gen = veval_cells(previous_gen,live_neighbor_counts)

    # Update board visualization
    board = next_gen
    img.set_data(board)
    plt.draw()
    plt.pause(.01)