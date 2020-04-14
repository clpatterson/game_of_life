import numpy as np

# Create a 2 x 2 2d matrix where values can either be 0 or 1
board = np.random.randint(2, size=(2,2))
# print(board)

# step 1: provide x,y coordinates for a cell to evaluate
cell_coordinates = (1,1)

# step 2: get the value for that cell
cell = board[cell_coordinates[1]][cell_coordinates[0]]

board[cell_coordinates[1]][cell_coordinates[0]] = 3

print(board)

# print("cell",cell)

# Coordinate ransformations to get neighbors
# nw = 
# w  = (-1,0)
# sw = 
# n  = (0,-1)
# s  = (0,+1)
# ne = 
# e  = (+1,0)
# se = 

# How do you do addition across arrays?




 # nw = board[cell_coordinates[1] - 1][cell_coordinates[0] - 1]
 # w = board[cell_coordinates[1] - 1][cell_coordinates[0]]
 # sw = board[cell_coordinates[1] - 1][cell_coordinates[0] + 1]
 # n = board[cell_coordinates[1]][cell_coordinates[0] - 1]
 # s = board[cell_coordinates[1]][cell_coordinates[0] + 1]
 # ne = board[cell_coordinates[1] + 1][cell_coordinates[0] - 1]
 # e = board[cell_coordinates[1] - 1][cell_coordinates[0]]
 # se = board[cell_coordinates[1] - 1][cell_coordinates[0] + 1]
# Use np.where() to get the index of a given cell



# How do I evaluate a single cell? I need to find all neighboors.
# List a cell's neighboors:
#  Game of life uses the Moore Neighborhood 
#  (a central cell and eight surrounding cells)
# Neighbors are:
# northwest
# west
# southwest
# north
# south
# northeast
# east
# southeast 

class Board():
	def __init__(self,size):
		self.board = np.random.randint(2, size=size)
		self.north_transform = (0,-1)
		self.south_transform = (0,1)
		self.east_transform = (1,0)
		self.west_transform = (-1,0)
	
	def get_cell_value(self,cell_coordinates):
		return self.board[cell_coordinates[1]][cell_coordinates[0]]

	def transform_coordinate(sefl, coord_one, coord_two):
		# Add coordinates together and return result
		return tuple(map(lambda x,y: x + y, coord_one, coord_two))

	def get_neighbor_coord(self,cell_coordinates,direction):
		if direction == 'n':
			cell_coordinates = self.transform_coordinate(cell_coordinates, self.north_transform)
		elif direction == 's':
			cell_coordinates = self.transform_coordinate(cell_coordinates, self.south_transform)
		elif direction == 'e':
			cell_coordinates = self.transform_coordinate(cell_coordinates, self.east_transform)
		elif direction == 'w':
			cell_coordinates = self.transform_coordinate(cell_coordinates, self.west_transform)
		elif direction == 'nw':
			ordinal_coord = self.transform_coordinate(self.north_transform, self.west_transform)
			cell_coordinates = self.transform_coordinate(cell_coordinates, ordinal_coord)
		elif direction == 'ne':
			ordinal_coord = self.transform_coordinate(self.north_transform, self.east_transform)
			cell_coordinates = self.transform_coordinate(cell_coordinates, ordinal_coord)
		elif direction == 'sw':
			ordinal_coord = self.transform_coordinate(self.south_transform, self.west_transform)
			cell_coordinates = self.transform_coordinate(cell_coordinates, ordinal_coord)
		elif direction == 'se':
			ordinal_coord = self.transform_coordinate(self.south_transform, self.east_transform)
			cell_coordinates = self.transform_coordinate(cell_coordinates, ordinal_coord)
		return cell_coordinates

	def get_all_neighbor_coord(self,cell_coordinates):
		neighbor_values = [self.get_neighbor_coord(cell_coordinates,direction)
		                   for direction in ["n","s","e","w","nw","ne","sw","se"]]
		return neighbor_values

	def get_live_neighbor_count(self,neighbor_coordinates):
		live_neighbor_count = 0
		for neighbor in neighbor_coordinates:
			try:
				value = self.get_cell_value(neighbor)
				if value == 1:
					live_neighbor_count += value
				else:
					continue
			except IndexError: # Some cells don't have 8 neighbors
				continue
		return live_neighbor_count

	def update_cell_value(self,cell_coordinates,new_value):
		self.board[cell_coordinates[1]][cell_coordinates[0]] = new_value
		return None

# Test Board Class

tb = Board((2,2))

print(tb.board)

print(tb.get_cell_value((1,1)))

print(tb.get_all_neighbor_coord((1,1)))

print(tb.get_live_neighbor_count(tb.get_all_neighbor_coord((1,1))))

