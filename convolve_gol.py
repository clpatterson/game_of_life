import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d


size = 100
generations = 100
board = np.random.randint(2, size=(size,size))
plt.ion() # set matplotlib to interactive mode
img = plt.imshow(board)

for i in range(generations + 1):
    next_gen = board.copy()
    print("starting_state:\n",next_gen)
    # Produce a board where each cell is filled with live neigbor count
    neighbor_counts = (convolve2d(next_gen, np.ones((3,3)), mode="same") - next_gen) #>= 3
    print ("neighbor_counts:\n",neighbor_counts)
    # TODO: how can this be faster than O(n)
    with np.nditer([next_gen,neighbor_counts], op_flags=['readwrite']) as it:
        for cell,count in it:
            if cell == 0 and count == 3:
                cell[...] = 1 # Reproduction
            elif cell == 1 and  count < 2 or count > 3:
                cell[...] = 0 # Death from under/over population
            else:
                pass

    board = next_gen
    print(board)
    img.set_data(board)
    plt.draw()
    plt.pause(.01) # TODO: allow user to set game speed