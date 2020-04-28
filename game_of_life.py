
"""A Conway's Game of Life board class.

This module provides a basic board class that tracks
the state of the board (between generations). The board
class provides the methods for getting a cells live
neighbor count and updating a cells value.

# TODO: Add type annotations

"""

import itertools
import numpy as np

class Board():
    """Conway's Game of Life board."""

    def __init__(self, size):
        self.board = np.random.randint(2, size=(size,size))
        self.board_size = size
        # Get all coordinate transformations for Moore neighbors 
        self.directions = [(x, y) 
                           for x, y in itertools.product([-1, 0, 1], [-1, 0, 1])
                           if x != 0 or y != 0]
    
    def get_cell_value(self, cell_coordinates):
        """Return cell value for given coordinates."""
        return self.board[cell_coordinates] # ndarrays take tuple indicies

    def get_all_neighbor_coord(self, cell_coordinates):
        """Return list of all Moore neighbor coordinates for given cell."""
        # Apply transformations to provided cell coordinates
        # Modulo board size creates an infinite/repeating board
        neighbor_coordinates = [((cell_coordinates[0] + x) % self.board_size, 
                                 (cell_coordinates[1] + y) % self.board_size) 
                                for x,y in self.directions]
        return neighbor_coordinates

    def get_live_neighbor_count(self, cell_coordinates):
        """Return a count of live neighbors."""
        neighbor_coordinates = self.get_all_neighbor_coord(cell_coordinates)
        live_neighbor_count = 0
        for neighbor in neighbor_coordinates:
            value = self.get_cell_value(neighbor)
            if value == 1:
                live_neighbor_count += value
            else:
                continue
        return live_neighbor_count

    def update_cell_value(self, cell_coordinates, new_value):
        """Update cell value with given new value."""
        self.board[cell_coordinates] = new_value
        return None

# # Test Board Class

# tb = Board(4)

# print(tb.board)

# print(tb.get_cell_value((0,0)))

# print(tb.get_all_neighbor_coord((0,0)))

# print(tb.get_live_neighbor_count((0,0)))

# tb.update_cell_value((0,0), 3)

# print(tb.board)

