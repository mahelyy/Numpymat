import numpy as np
from numpy import random

if __name__ == '__main__':
	grid = np.array ([])
	nameList = ["Emma", "Jace", "Timmy", "Grace", "Jenna","Sally",
		    "Jay", "Mia", "Stawberry", "Ella", "Harper", "Lucas"]

rows = int(input("Enter numbers of rows: "))
cols = int(input("Enter numbers of chairs per row: "))

for _ in range(rows):
	for _ in range(cols):
		randName = random.choice(nameList)
		grid = np.append(grid, randName)
		nameList.remove(randName)

grid = grid.reshape(rows, cols)


for i in range(rows):
	line = []
	for j in range(cols):
		line.append(f"{grid[i,j]} ({i},{j})")
	print(" ".join(line))
