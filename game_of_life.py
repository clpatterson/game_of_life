import numpy as np

class Board():
	def __init__(self,size):
		self.board = np.random.randint(2, size=size)
		self.north_transform = (0,-1)
		self.south_transform = (0,1)
		self.east_transform = (1,0)
		self.west_transform = (-1,0)
	
	def get_cell_value(self,cell_coordinates):
		return self.board[cell_coordinates] # ndarrays take tuple indicies

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
		neighbor_coordinates = [self.get_neighbor_coord(cell_coordinates,direction)
		                   for direction in ["n","s","e","w","nw","ne","sw","se"]]
		# Neighbor coordinates should never be negative                   
		neighbor_coordinates = [coord for coord in neighbor_coordinates if all( num >= 0 for num in coord)]
		return neighbor_coordinates

	def get_live_neighbor_count(self,cell_coordinates):
		neighbor_coordinates = self.get_all_neighbor_coord(cell_coordinates)
		live_neighbor_count = 0
		for neighbor in neighbor_coordinates:
			value = self.get_cell_value(neighbor)
			if value == 1:
				live_neighbor_count += value
			else:
				continue
		return live_neighbor_count

	def update_cell_value(self,cell_coordinates,new_value):
		self.board[cell_coordinates] = new_value
		return None

# # Test Board Class

# tb = Board((2,2))

# print(tb.board)

# print(tb.get_cell_value((0,0)))

# print(tb.get_all_neighbor_coord((0,0)))

# print(tb.get_live_neighbor_count((0,0)))

# tb.update_cell_value((0,0), 3)

# print(tb.board)

