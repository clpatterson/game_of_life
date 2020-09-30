"""Conway's Game of Life interface.

This module contains the user inferface for the game as well as
the rules for how the next generation is created. The rules of the 
game are as follows:

    1) Any live cell with two or three live neighbors survives.
    2) Any dead cell with three live neighbors becomes a live cell.
    3) All other live cells die in the next generation. Similarly, 
    all other dead cells stay dead.

After each generation the board is updated for the user to see. 

TODO: Implement as web app with Javascript (React?) frontend.
"""

import matplotlib.pyplot as plt
import numpy as np
import game_of_life

# Global game variables
size = 100
generations = 150
speed = 0.1

print("Let the Game of life begin!")

game = game_of_life.Board(size) # Initialize with randomly seeded board
plt.ion() # set matplotlib to interactive mode
img = plt.imshow(game.board) # Show the game board as image

for n in range(generations): # Set number of generations / life cycles to play
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
    plt.pause(speed) # Slow game down so player can see generations

#TODO: preserve final generation image.